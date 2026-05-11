def filter_techniques(problem: str, techniques: list[str]) -> list[str]:
    problem_lower = problem.lower()

    filtered = []

    for tech in techniques:
        t = tech.lower()

        if "prime" in problem_lower:
            if "prime" in t or "sqrt" in t or "mathematical" in t:
                filtered.append(tech)

        elif "array" in problem_lower:
            if "array" in t or "two pointers" in t or "sliding window" in t:
                filtered.append(tech)

        elif "dp" in problem_lower:
            if "dynamic programming" in t:
                filtered.append(tech)

    
    return filtered if filtered else techniques[:1]
