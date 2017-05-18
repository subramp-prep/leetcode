# coding=utf-8
# Author: Jianghan LI
# Question: 035.Search_Insert_Position
# Date: 2017-05-06
# Complexity: O(logN)


class Solution(object):

    def searchInsert(self, nums, target, ind=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return ind
        if len(nums) == 1:
            return int(target > nums[0]) + ind
        mid = len(nums) / 2
        return self.searchInsert(nums[:mid], target, ind) if nums[mid] >= target else self.searchInsert(nums[mid:], target, ind + mid)
