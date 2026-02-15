from agents.generate_agent import generator_agent

agent = generator_agent()

problem = "Longest Palindromic Substring"

plan = """
Use a dynamic programming approach.
Track palindromic substrings.
Return the longest one.
"""

code = agent({
    "problem": problem,
    "plan": plan
})

print(code)
