def sanitize_code(code: str) -> str:
    """
    Safely clean LLM output while preserving valid Python structure.

    What this DOES:
    - Removes markdown fences (```python, ```)
    - Removes leading/trailing empty lines
    - Preserves indentation, colons, and control flow
    - Keeps function definitions fully intact

    What this DOES NOT do:
    - Does NOT remove lines ending with ':'
    - Does NOT guess English vs Python
    - Does NOT modify indentation
    """

    if not code:
        return ""

    lines = code.splitlines()
    clean_lines = []

    for line in lines:
        stripped = line.strip()

        # Remove markdown code fences
        if stripped.startswith("```"):
            continue

        # Remove obvious chat artifacts
        if stripped in {"Here is the solution:", "Solution:", "Answer:"}:
            continue

        clean_lines.append(line)

    # Remove leading/trailing empty lines
    while clean_lines and not clean_lines[0].strip():
        clean_lines.pop(0)

    while clean_lines and not clean_lines[-1].strip():
        clean_lines.pop()

    return "\n".join(clean_lines)
