# coding=utf-8
# Author: Jianghan LI
# Question: Q1
# Complexity: O(N)
# Date: 2017-10-15

import collections


class Solution(object):

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = len(nums)
        c = collections.Counter(nums)
        degree = max(c.values())
        possible = {i for i in c if c[i] == degree}
        first = {}
        last = {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
        return min(last[v] - first[v] + 1 for v in possible)

    def findShortestSubArray(self, nums):
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)


############ test case ###########
s = Solution()
print s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])  # 6
print s.findShortestSubArray([1, 2, 2, 3, 1])  # 2


############ comments ############
