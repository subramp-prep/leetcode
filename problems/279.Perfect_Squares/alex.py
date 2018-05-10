class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        def issq(n):
            x = int(n**.5)
            return x * x == n

        if issq(n):
            return 1

        dp = [0, 1]
        for i in xrange(2, n + 1):
            if issq(i):
                ans = 1
            else:
                ans = 4
                for k in xrange(1, int(i**.5) + 1):
                    t = i - k * k
                    ans = min(ans, dp[t] + 1)

            dp.append(ans)
        return dp[-1]
