# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-21

import itertools


class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(2, len(nums) + 1):
            ret += list(set(itertools.combinations(nums, i)))

        def isIncreasing(l):
            for i in range(1, len(l)):
                if l[i - 1] > l[i]:
                    return False
            return True
        return [x for x in ret if isIncreasing(x)]

    def findSubsequences(self, nums):
        ret = [l for i in range(2, len(nums) + 1) for l in set(itertools.combinations(nums, i))]
        return [l for l in ret if all(l[i - 1] <= l[i] for i in range(1, len(l)))]


############### test cases ###################
s = Solution()
print s.findSubsequences([1, 2, 3, 4])

# brute force 暴力搜索
# 用itertools枚举所有combination
