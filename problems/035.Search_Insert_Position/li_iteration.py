# coding=utf-8
# Author: Jianghan LI
# Question: 035.Search_Insert_Position
# Date: 2017-05-06
# Complexity: O(NlogN)


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ind = 0
        while len(nums):
            mid = len(nums) / 2
            if nums[mid] >= target:
                nums = nums[:mid]
            else:
                nums = nums[mid + 1:]
                ind += mid + 1
        return ind
