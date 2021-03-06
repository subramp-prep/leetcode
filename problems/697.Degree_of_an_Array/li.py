# coding=utf-8
# Author: Jianghan LI
# Question: 697.Degree_of_an_Array
# Complexity: O(N) O(M)
# Date: 2017-10-15

import collections


class Solution(object):

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)


############ test case ###########
s = Solution()
print s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])  # 6
print s.findShortestSubArray([1, 2, 2, 3, 1])  # 2


############ comments ############
