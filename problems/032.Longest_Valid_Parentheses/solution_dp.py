def longestValidParentheses(self, s):
    dp, s = [0], ')' + s
    for i in xrange(1, len(s), 1):
        if s[i] == ')' and s[i - dp[-1] - 1] == '(':
            dp.append(dp[-1] + 2 + dp[-2 - dp[-1]])
        else:
            dp.append(0)
    return max(dp)


def longestValidParentheses(self, s):
    s = ')' + s
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')' and s[i - dp[i - 1] - 1] == '(':
            dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
    return max(dp)
