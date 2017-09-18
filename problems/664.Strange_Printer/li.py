class Solution(object):

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(a for a, b in zip(s, s[1:] + '#') if a != b)
        self.dp = {}

        def dp(i, j):
            return self.dp.get((i, j), j - i)

        for l in range(2, len(s)):
            for i in range(len(s) - l):
                res = dp(i, i + l) + 1
                for j in range(i, i + l):
                    if s[j] == s[i + l]:
                        res = min(res, dp(i, j) + dp(j + 1, i + l + 1))
                self.dp[i, i + l + 1] = res
        return dp(0, len(s))



# 研究s[i:i+l+1]的次数，初始值是s[i:i+l]结果+1。
# 遍历s[i:i+l]，看看有没有和s[i+l]一样的字母。
