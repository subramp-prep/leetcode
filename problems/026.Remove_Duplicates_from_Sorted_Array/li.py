# coding=utf-8
# Author: Jianghan LI
# Question: 026.Remove_Duplicates_from_Sorted_Array
# Complexity: O(N)
# Date:  2017-10-11


class Solution(object):

    # pop, O(N^2)
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        while i + 1 < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums.pop(i)
            i += 1
        return len(nums)

    # two pointer, while loop, O(N)
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return i + 1

    # two pointer, for loop, solution 12672, O(N)
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
