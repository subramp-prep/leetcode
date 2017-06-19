# coding=utf-8
# Author: Jianghan LI
# Question: 189.Rotate_Array
# Date: 2017-06-07 09:08 - 09:08, 0 wrong try
# Complexity: O(N)


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
