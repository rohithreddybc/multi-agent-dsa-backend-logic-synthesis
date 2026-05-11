from agents.review_agent import reviewer_agent

reviewer = reviewer_agent()

good = reviewer.invoke({
    "code": "def add(a, b): return a + b"
})

bad = reviewer.invoke({
    "code": "def add(a, b): return a - b"
})

print("GOOD:", good.content)
print("BAD:", bad.content)
