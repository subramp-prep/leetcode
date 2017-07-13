# coding=utf-8
# Author: Jianghan LI
# Question: 640.Solve_the_Equation
# Date: 2017-07-12

import re


class Solution(object):

    def solveEquation(self, eqa):
        """
        :type equation: str
        :rtype: str
        """
        eqa = re.sub("(\d)x", r'\1*x', eqa)
        left, right = eqa.split('=')
        eqa = left + '-(' + right + ')'
        y0, y1 = eval(eqa.replace('x', '0')), eval(eqa.replace('x', '1'))
        if y0 == y1 == 0:
            return "Infinite solutions"
        if y0 == y1:
            return "No solution"
        return 'x=%d' % (y0 / (y0 - y1))


############ test case ###########
Input1 = "x+5-3+x=6+x-2"  # "x=2"
Input2 = "x=x"  # "Infinite solutions"
Input3 = "2x=x"  # "x=0"
Input4 = "2x+3x-6x=x+2"  # "x=-1"
Input5 = "x=x+2"  # "No solution"

s = Solution()
print s.solveEquation(Input1)
