"""Sandbox safety + correctness tests."""

from __future__ import annotations

from execugraph.execution.sandbox import run_in_sandbox


def test_valid_function_call() -> None:
    r = run_in_sandbox("def f(n): return n*n", call="f(7)")
    assert r.ok
    assert r.return_value == 49
    assert r.error_class == "none"


def test_blocks_os_import() -> None:
    r = run_in_sandbox("import os\nx = os.getcwd()", call="x")
    assert not r.ok
    assert r.error_class == "sandbox_violation"
    assert "sandbox" in r.stderr.lower()


def test_blocks_subprocess_import() -> None:
    r = run_in_sandbox("import subprocess", call=None)
    assert not r.ok
    assert r.error_class == "sandbox_violation"


def test_blocks_socket_import() -> None:
    r = run_in_sandbox("import socket", call=None)
    assert not r.ok


def test_runtime_error_classified() -> None:
    r = run_in_sandbox("def f():\n    return 1/0", call="f()")
    assert not r.ok
    assert r.error_class == "runtime"


def test_syntax_error_classified() -> None:
    r = run_in_sandbox("def broken(:", call="broken()")
    assert not r.ok
    assert r.error_class == "syntax"


def test_timeout() -> None:
    r = run_in_sandbox("while True: pass", call=None, timeout_s=1.0)
    assert not r.ok
    assert r.error_class == "timeout"


def test_allowed_module_import() -> None:
    r = run_in_sandbox(
        "from collections import deque\n"
        "def f(): q = deque([1,2,3]); return list(q)",
        call="f()",
    )
    assert r.ok, r.stderr
    assert r.return_value == [1, 2, 3]


def test_open_is_removed() -> None:
    r = run_in_sandbox("def f(): return open('x')", call="f()")
    assert not r.ok
