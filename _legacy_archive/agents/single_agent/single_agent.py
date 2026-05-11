from util.llm import get_llm
def single_agent_generate(problem: str):
    """
    Single-agent, single-pass code generation.
    No planning, no review, no execution, no retries.
    """

    llm = get_llm(role="generator")

    prompt = f"""
                You are an expert software engineer.
                Solve the following problem.
                Generate ONLY Python code.
                Do NOT include explanations or comments.

            Problem:
            {problem}
            """

    response = llm.invoke(prompt)

    return response.content
