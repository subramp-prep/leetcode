# coding=utf-8
# Author: Jianghan LI
# Question: 632.Smallest_Range
# Date: 2017-07-03 14:17 - 14:30
# Complexity: O(N)


class Solution(object):

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, int((c / 2) ** 0.5) + 1):
            if self.isSquare(c - i * i):
                return True
        return False

    def isSquare(self, c):
        return int(c**0.5)**2 == c
