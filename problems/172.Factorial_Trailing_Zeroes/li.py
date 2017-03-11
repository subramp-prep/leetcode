# coding=utf-8
# Author: Han
# Question: 172. Factorial Trailing Zeroes
# Date: 2017-03-11
# Complexity: O(LogN)


class Solution(object):

    def trailingZeroes(self, n):
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r

s = Solution()
print s.trailingZeroes(10)


print 2**32
print 5**15
