# coding=utf-8
# Author: Jianghan LI
# Question: 089.Gray_Code
# Date: 23/03/2017 9:04 - 9:09
# Complexity: O(2^N)


class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        tmp = self.grayCode(n - 1)
        return tmp + [i + 2**(n - 1) for i in reversed(tmp)]
