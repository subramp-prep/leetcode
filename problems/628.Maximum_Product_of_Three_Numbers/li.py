# coding=utf-8
# Author: Jianghan LI
# Question: 628.Maximum_Product_of_Three_Numbers
# Date: 2017-06-27 14:38 - 14:43, 1 wrong try
# Complexity: O(N)


class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])`

# 1 wrong try: sort is ascendent.
