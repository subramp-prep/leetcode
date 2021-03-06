# coding=utf-8
# Author: Jianghan LI
# Question: 365.Water_and_Jug_Problem
# Date: 2017-04-14
# Complexity: O(logN)


class Solution(object):

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def hcf(x, y):
            while x and y:
                x, y = min(x, y), max(x, y) % min(x, y)
            return x + y
        hcf = hcf(x, y)
        return z == 0 or hcf != 0 and z % hcf == 0 and x + y >= z

    def canMeasureWater(self, x, y, z):
        gcd, r = max(x, y), min(x, y)
        while r:
            gcd, r = r, gcd % r
        return z == 0 or x + y >= z and z % gcd == 0

    def canMeasureWater(self, x, y, z):
        s = x + y
        while x:
            x, y = y % x, x
        return z == 0 or s >= z and z % y == 0

# 辗转相除算最大公约数
# 辗转相处最慢递降是斐波纳切变型逆序，所以递降复杂度是logN
