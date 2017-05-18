# coding=utf-8
# Author: Jianghan LI
# Question: 583.Delete_Operation_for_Two_Strings
# Date: 2017-05-17 14:30 - 14:46

# Complexity: O(MN)


class Solution(object):

    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] +
                                       1, dp[i][j] + 2 * (w1[i] != w2[j]))
        return dp[m][n]

    def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
        return m + n - 2 * dp[m][n]

# Penalty: 1 wrong try
# dp initialization, n first m second
