import re

def extract_python_code(text: str) -> str:
    """
    Safely extract Python code from LLM output without breaking indentation
    or control-flow structure.
    """

    if not text:
        return ""

    # 1. Prefer fenced python blocks
    fenced = re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    if fenced:
        return fenced[0].strip()

    # 2. Otherwise, assume the model followed instructions
    # and returned raw Python code only.
    # DO NOT filter lines — preserve structure.
    lines = text.splitlines()

    # Remove leading/trailing non-code noise
    while lines and not lines[0].strip():
        lines.pop(0)

    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines)
