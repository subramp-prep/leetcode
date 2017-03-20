# coding=utf-8
# Author: Jianghan LI
# Question: 153.Find_Minimum_in_Rotated_Sorted_Array
# Date: 2017-03-16
# Complexity: O(N)


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
