#!/usr/local/bin/python3
# coding=utf-8
# Author: Jianghan LI
# Question: 592.Fraction_Addition_and_Subtraction
# Date: 2017-05-23
# Complexity: O(N)

import math


class Solution(object):

    def fractionAddition(self, exp):
        i, j, a, b, n = 0, 0, 0, 1, len(exp)
        while j < len(exp):
            i, j = j, exp.find('/', j)
            a2 = int(exp[i:j])
            i, j = j + 1, min(exp.find('+', j) % (n + 1), exp.find('-', j) % (n + 1))
            b2 = int(exp[i:j])
            a, b = a * b2 + b * a2, b * b2
            a, b = a // math.gcd(a, b), b // math.gcd(a, b)
        return str(a) + '/' + str(b)


############ test case ###########
s = Solution()
print(s.fractionAddition("-1/2+1/2"))

############ comments ############
