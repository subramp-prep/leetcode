# coding=utf-8
# Author: Jianghan LI
# Question: 072.Edit_Distance
# Complexity: O(N)
# Date: 2017-09-06 8:01 - 8:11, 0 wrong try


class Solution(object):

    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(w1) + 1, len(w2) + 1
        d = [[0 for j in range(n)] for i in range(m)]
        for i in range(m): d[i][0] = i
        for j in range(n): d[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (w1[i - 1] != w2[j - 1]))
        return d[m - 1][n - 1]
