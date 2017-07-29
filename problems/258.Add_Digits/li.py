# coding=utf-8
# Author: Jianghan LI
# Question: 258.Add_Digits
# Complexity: O(N)
# Date: 2017-07-08 02:39 - 02:39


class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 or 9 if num else 0
