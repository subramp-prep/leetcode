# coding=utf-8
# Author: Jianghan LI
# Question: 769.Max_Chunks_To_Make_Sorted
# Complexity: O(N)
# Date: 2018-01-21 0:22:08 - 0:28:40, 1 wrong try

from functools import reduce


class Solution(object):

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curMax = -1
        res = 0
        for i, v in enumerate(arr):
            curMax = max(curMax, v)
            if curMax == i:
                res += 1
        return res

    def maxChunksToSorted(self, arr):
        curMax, res = -1, 0
        for i, v in enumerate(arr):
            curMax = max(curMax, v)
            res += curMax == i
        return res

    def maxChunksToSorted(self, arr):
        return reduce(lambda (curMax, res), (i, v): (max(curMax, v), res + (max(curMax, v) == i)), enumerate(arr), (-1, 0))[1]

    def maxChunksToSorted(self, arr):
        return sum(max(arr[:i + 1]) == i for i in range(len(arr)))


############ test case ###########
s = Solution()
print s.maxChunksToSorted([1, 0, 2, 3, 4])  # 4
print s.maxChunksToSorted([4, 3, 2, 1, 0])  # 1
print s.maxChunksToSorted([0, 1, 2, 3])  # 4
print s.maxChunksToSorted([1, 2, 0, 3])  # 2


############ comments ############
