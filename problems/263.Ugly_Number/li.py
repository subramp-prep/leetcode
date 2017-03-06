# coding=utf-8
# Author: Jianghan LI
# Question: 263.Ugly_Number
# Date: 2017-03-06 22:07 - 22:10
# Complexity: O(logN)


class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
