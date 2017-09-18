# coding=utf-8
# Author: Jianghan LI
# Question: 672.Bulb_Switcher_II
# Complexity: O(1)
# Date: 2017-09－03
# Contest48 0:20:28 - 0:43:31, 3 wrong try

class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n==0 or m==0: return 1
        if n==1: return 2
        if n==2 and m==1: return 3
        if n==2 or m==1: return 4
        if n>=3 and m==2: return 7
        return 8

    def flipLights(self, n, m):
        if n==0 or m==0: return 1
        if n==1: return 2
        if n==2 and m==1: return 3
        if n==2 or m==1: return 4
        if m==2: return 7
        return 8
