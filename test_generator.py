from agents.generate_agent import generator_agent

agent = generator_agent()

result = agent.invoke({
    "problem": "Longest Palindromic Substring",
    "techniques": ""
})

print(result.content)
