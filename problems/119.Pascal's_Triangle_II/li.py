# coding=utf-8
# Author: Jianghan LI
# Question: 119.Pascal's_Triangle_II/li.py
# Complexity: O(N)
# Date: 2017-08-28 10:30 - 10:33, 0 wrong try


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1]
        for _ in range(rowIndex):
            cur = [a + b for a, b in zip([0] + cur, cur + [0])]
        return cur
