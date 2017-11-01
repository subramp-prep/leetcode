# coding=utf-8
# Author: Jianghan LI
# Question: 373.Find_K_Pairs_with_Smallest_Sums/li.py
# Date: 03/03/2017 00:47
# Complexity: O(K^2logK) O(K)

import itertools
import heapq


class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum)

    def kSmallestPairs(self, nums1, nums2, k):
        return heapq.nsmallest(k, itertools.product(nums1[:k], nums2[:k]), key=sum)


############ test case ###########
s = Solution()
print s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
print s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2)

############ comments ############
