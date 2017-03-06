# coding=utf-8
# Author: Jianghan LI
# Question: 202.Happy_Number
# Date: 06/03/2017


class Solution(object):

    def isHappy(self, n):
        while n > 4:
            n = sum(int(x) ** 2 for x in str(n))
        return n == 1

s = Solution()
print s.isHappy(7)
