# coding=utf-8
# Author: Jianghan LI
# Question: 532.K-diff_Pairs_in_an_Array
# Date: 08/03/2017 13:25-13:33

import collections


class Solution(object):

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k > 0:
            nums = set(nums)
            for i in nums:
                if i + k in nums:
                    res += 1
        elif k == 0:
            c = collections.Counter(nums)
            for i in c:
                if c[i] > 1:
                    res += 1
        return res

    def findPairs2(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

    def findPairs3(self, nums, k):
        c = collections.Counter(nums)
        return sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
