"""Subprocess-isolated sandbox for executing LLM-generated Python.

Generated code is sent to a freshly forked Python interpreter via stdin.
The child enforces a wall-clock timeout, a curated ``__builtins__``, and
denies imports of dangerous modules. Communication is JSON over stdout.

This is *not* a kernel-level container; see
``paper/sections/06_discussion_limitations.tex`` for limitations. It is
sufficient to keep the Evaluator's loop honest and to prevent accidental
filesystem / network damage during long unsupervised experiment runs.
"""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass

# Modules the child interpreter is allowed to import. Anything not in this
# set causes ``__import__`` to raise. ``builtins`` is allowed implicitly.
_ALLOWED_MODULES = frozenset(
    {
        "math",
        "collections",
        "heapq",
        "bisect",
        "functools",
        "itertools",
        "operator",
        "random",
        "re",
        "string",
        "typing",
        "dataclasses",
        "fractions",
        "decimal",
        "statistics",
        "numbers",
        "copy",
        "json",
        # Needed for APPS-style stdin/stdout problems:
        "sys",
        "io",
    }
)


@dataclass
class SandboxResult:
    ok: bool
    stdout: str
    stderr: str
    error_class: str  # one of: none, syntax, runtime, timeout, sandbox_violation
    return_value: object = None


_CHILD_PRELUDE = textwrap.dedent(
    """
    import sys, json, builtins, traceback

    _ALLOWED = {allowed}
    _real_import = builtins.__import__
    def _guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
        root = name.split('.')[0]
        if root not in _ALLOWED:
            raise ImportError(f"sandbox: import of '{{root}}' is not permitted")
        return _real_import(name, globals, locals, fromlist, level)
    builtins.__import__ = _guarded_import

    for _bad in ("eval","exec","compile","open","input","breakpoint"):
        if hasattr(builtins, _bad):
            try: delattr(builtins, _bad)
            except Exception: pass

    payload = json.loads(sys.stdin.read())
    user_code = payload["code"]
    user_call = payload.get("call")

    try:
        compiled = _real_import("builtins").__dict__.get("compile", None)
        # compile/exec are needed once to install the function; they were
        # removed above, so we re-introduce them locally then drop.
        import types
        ns = {{}}
        code_obj = types.CodeType  # noqa: F841 (exists check)
        # Use types via marshal-free path: rebuild compile by reimporting.
        import importlib
        _builtins_mod = importlib.import_module("builtins")
        _compile = _real_import("builtins").__dict__.get("__class__")  # placeholder

        # We re-enable compile + exec just inside this try, scoped to ns.
        _compile_fn = compile if 'compile' in dir(__builtins__) else None
    except Exception as e:
        sys.stdout.write(json.dumps({{
            "ok": False,
            "stdout": "",
            "stderr": "sandbox bootstrap failed: " + repr(e),
            "error_class": "sandbox_violation",
            "return_value": None,
        }}))
        sys.exit(0)
    """
).strip()


# A simpler, robust child program: we keep `compile` and `exec` available
# inside the child for the user's source compilation step, but we still
# strip the truly dangerous primitives and gate ``__import__``.
_CHILD_PROGRAM = textwrap.dedent(
    """
    import sys, json, builtins, traceback, io, contextlib

    _ALLOWED = set({allowed!r})
    _real_import = builtins.__import__

    def _guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
        root = name.split('.')[0]
        if root not in _ALLOWED:
            raise ImportError("sandbox: import of '" + root + "' is not permitted")
        return _real_import(name, globals, locals, fromlist, level)

    builtins.__import__ = _guarded_import
    for _name in ("open", "input", "breakpoint"):
        if hasattr(builtins, _name):
            try: delattr(builtins, _name)
            except Exception: pass

    payload = json.loads(sys.stdin.read())
    user_code = payload["code"]
    user_call = payload.get("call")

    ns = {{"__name__": "__sandbox__"}}
    out = io.StringIO()
    err = io.StringIO()
    result = {{
        "ok": False, "stdout": "", "stderr": "",
        "error_class": "none", "return_value": None,
    }}
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                exec(compile(user_code, "<sandbox>", "exec"), ns, ns)
            except SyntaxError:
                raise
            if user_call is not None:
                try:
                    rv = eval(user_call, ns, ns)
                except Exception:
                    raise
                try:
                    json.dumps(rv)
                    result["return_value"] = rv
                except TypeError:
                    result["return_value"] = repr(rv)
        result["ok"] = True
    except SyntaxError as e:
        result["error_class"] = "syntax"
        result["stderr"] = "{{}}: {{}}".format(type(e).__name__, e)
    except ImportError as e:
        msg = str(e)
        result["error_class"] = "sandbox_violation" if "sandbox" in msg else "runtime"
        result["stderr"] = msg
    except Exception as e:
        result["error_class"] = "runtime"
        result["stderr"] = "{{}}: {{}}\\n{{}}".format(
            type(e).__name__, e, traceback.format_exc(limit=4)
        )
    result["stdout"] = out.getvalue()
    if not result["stderr"]:
        result["stderr"] = err.getvalue()
    sys.stdout.write(json.dumps(result, default=str))
    """
).strip()


def run_in_sandbox(
    code: str,
    *,
    call: str | None = None,
    timeout_s: float = 5.0,
    allowed_modules: frozenset[str] = _ALLOWED_MODULES,
) -> SandboxResult:
    """Run ``code`` in a child python and optionally evaluate ``call`` on the resulting namespace."""
    program = _CHILD_PROGRAM.format(allowed=tuple(sorted(allowed_modules)))
    payload = json.dumps({"code": code, "call": call})
    try:
        proc = subprocess.run(
            [sys.executable, "-I", "-c", program],
            input=payload,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        return SandboxResult(
            ok=False, stdout="", stderr="timeout", error_class="timeout"
        )
    stdout = proc.stdout.strip()
    if not stdout:
        return SandboxResult(
            ok=False,
            stdout="",
            stderr=proc.stderr or "child produced no output",
            error_class="runtime",
        )
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return SandboxResult(
            ok=False, stdout=stdout, stderr=proc.stderr, error_class="runtime"
        )
    return SandboxResult(
        ok=bool(data.get("ok")),
        stdout=data.get("stdout", ""),
        stderr=data.get("stderr", ""),
        error_class=data.get("error_class", "runtime"),
        return_value=data.get("return_value"),
    )
