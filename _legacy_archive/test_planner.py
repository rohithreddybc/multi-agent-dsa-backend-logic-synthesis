from agents.planner_agent import planner_agent

agent = planner_agent()

problem = "Longest Palindromic Substring"

result = agent.invoke({"problem": problem})

print(result.content)
