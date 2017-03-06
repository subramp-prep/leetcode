# coding=utf-8
# Author: Jianghan LI
# Question: 263.Ugly_Number
# Date: 2017-03-06
# Complexity: O(1)


class Solution(object):

    def isUgly(self, num):
        return num > 0 and 30**32 % num == 0

# In fact, (2*3*5)**20 is big enough for test case.
