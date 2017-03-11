# coding=utf-8
# Author: Han
# Question: 172. Factorial Trailing Zeroes
# Date: 2017-03-11
# Complexity: O(LogN)


class Solution(object):

    def trailingZeroes(self, n, ret=0):
        return self.trailingZeroes(n / 5, ret + n // 5) if n else ret
