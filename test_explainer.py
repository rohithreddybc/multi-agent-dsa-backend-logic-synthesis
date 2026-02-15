from agents.explainer_agent import explainer_agent

agent = explainer_agent()

problem = "Longest Palindromic Substring"

code = """
def longestPalindrome(s):
    if not s:
        return ""
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    max_len = 1
    start = 0
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
    return s[start:start+max_len]
"""

result = agent.invoke({
    "problem": problem,
    "code": code
})

print(result.content)
