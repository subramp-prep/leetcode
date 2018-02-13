# coding=utf-8
# Author: Jianghan LI
# Question: 740.Delete_and_Earn
# Complexity: O(10000)
# Date: 2017-12-20


class Solution(object):

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        a = b = 0
        for i in range(1, 10001):
            a, b = b, max(b, a + c[i] * i)
        return b
