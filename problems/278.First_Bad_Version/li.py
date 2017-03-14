# coding=utf-8
# Author: Jianghan Li
# Question: 278. First Bad Version
# Date: 14/03/2017

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, right, left=1):
        """
        :type n: int
        :rtype: int
        """
        return right if right == left else self.firstBadVersion((left + right) / 2, left) if isBadVersion((left + right) / 2) else self.firstBadVersion(right, (left + right) / 2 + 1)
