from agents.review_agent import reviewer_agent

code = """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""
wrong_code = """
def add(a, b):
    return a - b
"""

agent = reviewer_agent()
result = agent.invoke({"code": code})
wrng_res = agent.invoke({'code':wrong_code})
print(result.content)
print(wrng_res.content)
