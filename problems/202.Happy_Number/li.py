# coding=utf-8
# Author: Jianghan LI
# Question: 202.Happy_Number
# Date: 06/03/2017 11:07 - 11:20


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen, n = set(), str(n)
        while 1:
            n = str(sum(map(lambda x: x * x, map(int, n))))
            if '1' == n:
                return True
            if n in seen:
                return False
            seen.add(n)

s = Solution()
print s.isHappy(2)
