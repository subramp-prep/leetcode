# coding=utf-8
# Author: Jianghan LI
# Question: 628.Maximum_Product_of_Three_Numbers
# Date: 2017-06-27 14:38 - 14:43, 1 wrong try
# Complexity: O(N)

import heapq


class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])

    def maximumProduct(self, nums):
        return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])

# 1 wrong try: sort is ascendent.
