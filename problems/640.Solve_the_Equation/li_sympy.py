# coding=utf-8
# Author: Jianghan LI
# Question: 640.Solve_the_Equation
# Date: 2017-07-12 16:20 - 16:51
# Complexity: O(N)

import sympy
import re


class Solution(object):

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        x = sympy.symbols('x')
        equation = re.sub("(\d)x", r'\1*x', equation)
        left, right = equation.split('=')
        ret = sympy.solve(eval(left + '-(' + right + ')'), x)
        if ret:
            return "x=%d" % ret[0]
        if eval(left.replace('x', '0')) == eval(right.replace('x', '0')):
            return "Infinite solutions"
        return "No solution"


############ test case ###########
Input1 = "x+5-3+x=6+x-2"  # "x=2"
Input2 = "x=x"  # "Infinite solutions"
Input3 = "2x=x"  # "x=0"
Input4 = "2x+3x-6x=x+2"  # "x=-1"
Input5 = "x=x+2"  # "No solution"

s = Solution()
print s.solveEquation(Input2)


############ comments ############
# Leetcode: No module named sympy
