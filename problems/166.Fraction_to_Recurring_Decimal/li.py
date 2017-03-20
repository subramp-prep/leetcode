# coding=utf-8
# Author: Jianghan LI
# Question: 166.Fraction_to_Recurring_Decimal
# Date: 2017-03-10
# Complexity: O(N) O(N)

import math


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        n1, n2 = abs(numerator), abs(denominator)
        if n1 % n2 == 0:
            return sign + str(n1 / n2)
        int_part = str(n1 // n2)
        n1 = n1 % n2
        remainder = {}
        ret = []
        pos = 0
        while n1 and n1 not in remainder:
            remainder[n1] = pos
            pos += 1
            ret.append(n1 * 10 // n2)
            n1 = n1 * 10 % n2
        float_part = ''.join(map(str, ret))
        if n1:
            float_part = float_part[:remainder[n1]] + '(' + float_part[remainder[n1]:] + ')'
        return sign + int_part + '.' + float_part

############ test case ###########
s = Solution()
print s.fractionToDecimal(1, 7)
