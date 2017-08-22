# coding=utf-8
# Author: Jianghan LI
# Question: 115.Distinct_Subsequences
# Complexity: O(MN)
# Date: 2017-08-04 11:43 - 11:54, 0 wrong try


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[1] + [0] * len(t) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
        return dp[-1][-1]
