

from agents.single_agent.single_agent import single_agent_generate

def run_single_agent(problem):
    print("\n=== SINGLE AGENT INPUT ===")
    print(problem)

    code = single_agent_generate(problem)

    print("\n=== SINGLE AGENT OUTPUT CODE ===")
    print(code)

    return code

if __name__ == "__main__":
    problem = """
Do not give any explanation give only standard python code,
Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.


    """

    run_single_agent(problem)
