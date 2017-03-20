# coding=utf-8
# Author: Jianghan LI
# Question: 154.Find_Minimum_in_Rotated_Sorted_Array_II
# Date: 2017-03-17
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
            elif nums[m] < nums[r]:
                r = m
            else:
                r = r - 1
        return nums[l]

# 始终拿中间的数和right的数相比
