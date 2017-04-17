# coding=utf-8
# Author: Jianghan LI
# Question: 343.Integer_Break
# Date: 2017-04-17


class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return (n - 1) * 1
        if n % 3 == 1:
            return 3**(n / 3) / 3 * 4
        if n % 3 == 2:
            return 3**(n / 3) * 2
        return 3**(n / 3)
