# coding=utf-8
# Author: Jianghan LI
# Question: 319.Bulb_Switcher
# Complexity: O(1)
# Date: 10:20 - 10:24

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))