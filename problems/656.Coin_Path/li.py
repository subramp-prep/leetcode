# coding=utf-8
# Author: Jianghan LI
# Question: 656.Coin_Path
# Complexity: O(N)
# Date:  2017-08-06

class Solution(object):

    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[0] == -1:
            return []
        dp = [[float('inf')] for i in A]
        dp[0] = [A[0], 1]
        N = len(A)
        for i in range(N):
            if A[i] == -1:
                continue
            for j in range(i + 1, min(N, i + B + 1)):
                if A[j] == -1:
                    continue
                if dp[i][0] + A[j] < dp[j][0]:
                    dp[j] = [dp[i][0] + A[j]] + dp[i][1:] + [j + 1]
                if dp[i][0] + A[j] == dp[j][0]:
                    path = dp[i][1:] + [j + 1]
                    if path < dp[j][1:]:
                        dp[j] = [dp[i][0] + A[j]] + dp[i][1:] + [j + 1]
        return dp[-1][1:]

    def cheapestJump(self, A, B):
        if not A or A[0] == -1:
            return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1: continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
        return dp[-1][1:] if dp[-1][0] < float('inf') else []


############ test case ###########
s = Solution()
print s.cheapestJump([1, 2, 4, -1, 2], 2)  # [1, 3, 5]
print s.cheapestJump([1, 2, 4, -1, 2], 1)  # []
print s.cheapestJump([0, 0, 0, 0, 0, 0], 2)  # [1, 2, 3, 4, 5, 6]

# If there are multiple paths with the same cost, return the lexicographically smallest such path.
