# coding=utf-8
# Author: Jianghan LI
# Question: 693.Binary_Number_with_Alternating_Bits
# Date: 2018-01-04


class Solution(object):

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return all(i != j for i, j in zip(bin(n)[2:], bin(n)[3:]))

    def hasAlternatingBits(self, n):
        return not (n * 3) & (n * 3 + 2 - n % 2)

    def hasAlternatingBits(self, n):
        return not (n * 3) & (n * 3 + 1) & (n * 3 + 2)
