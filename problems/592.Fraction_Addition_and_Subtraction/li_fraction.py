#!/usr/local/bin/python3
# coding=utf-8
# Author: Jianghan LI
# Question: 592.Fraction_Addition_and_Subtraction
# Date: 2017-05-23
# Complexity: O(N)

from fractions import Fraction


class Solution(object):

    def fractionAddition(self, exp):

        res = sum(map(Fraction, exp.replace('+', ' +').replace('-', ' -').split()))
        return str(res.numerator) + '/' + str(res.denominator)


############ test case ###########
s = Solution()
print(s.fractionAddition("-3/6+3/6"))
