# coding=utf-8
# Author: Jianghan LI
# Question: 768.Max_Chunks_To_Make_Sorted_II
# Complexity: O(NK)
# Date: 2018-01-21 0:28:40 - 0:36:17, 1 wrong try

import collections


class Solution(object):

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res, c1, c2 = 0, collections.Counter(), collections.Counter()
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            res += c1 == c2
        return res

############ test case ###########
s = Solution()
print s.maxChunksToSorted([5, 4, 3, 2, 1])  # 1

print s.maxChunksToSorted([2, 1, 3, 4, 4])  # 4

print s.maxChunksToSorted([1, 1, 0, 0, 1])  # 2

############ comments ############
