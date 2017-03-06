# coding=utf-8
# Author: Jianghan LI
# Question: 202.Happy_Number
# Date: 06/03/2017


class Solution(object):

    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return n == 1

s = Solution()
for i in range(100):
    s.isHappy(i)
