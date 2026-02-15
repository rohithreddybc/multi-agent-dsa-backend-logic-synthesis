from graph.workflow import app

state = {
    "problem": "Longest Palindromic Substring",
    "logs": [],
    "passed": False
}

result = app.invoke(state)

print("\n".join(result["logs"]))

print("\nFINAL CODE:\n")
print(result["code"])

if "explanation" in result:
    print("\nEXPLANATION:\n")
    print(result["explanation"])
else:
    print("\nEXPLANATION:\nNot generated (solution rejected)")
