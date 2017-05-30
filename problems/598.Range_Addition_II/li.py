# coding=utf-8
# Author: Jianghan LI
# Question: 598.Range_Addition_II
# Date: 2017-05-30 13:18 - 13:21, 0 wrong try
# Complexity: O(N)


class Solution(object):

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        return min(op[0] for op in ops) * min(op[1] for op in ops) if ops else m * n
