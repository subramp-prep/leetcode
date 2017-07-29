# coding=utf-8
# Author: Jianghan LI
# Question: 326.Power_of_Three
# Complexity: O(N)
# Date: 2017-06-29  9:07 - 9:16


class Solution(object):

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** round(math.log(n) / math.log(3)) == n
