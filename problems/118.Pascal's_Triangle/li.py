# coding=utf-8
# Author: Jianghan LI
# Question: 118.Pascal's_Triangle/li.py
# Date: 2017-06-10 11:35-11:39, 0 wrong try


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(numRows - 1):
            res.append([1] + [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)] + [1])
        return res
