def longestValidParentheses(self, s):
    dp, stack = [0] * (len(s) + 1), []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)

# let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s,
# then we have the following relationship:
# dp[i + 1] = dp[p] + i - p + 1
# where p is the position of '(' which can matches current ')' in the stack.


# AC_stack_n 也用到了stack 思路很不错
# (()）()对于这种情况，dp的思路是2＋4。
# AC_stack_n的思路是继续找stack的栈顶元素，栈顶标志了最后一个匹配的元素
