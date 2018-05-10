class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * n
        for x in range(1, n + 1):
            i = 1
            while i * i <= x:
                dp[x] = min(dp[x], dp[x - i * i] + 1)
                i += 1
        return dp[n]
