# coding=utf-8
# Author: Jianghan LI
# Question: 581.Shortest_Unsorted_Continuous_Subarray
# Date: 2017-05-17 10:27 - 10:31
# Penalty: 1 wrong try
# Complexity: O(NlogN)


class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                break
        if i == len(nums) - 1:
            return 0
        for j in range(len(nums)):
            if nums[-1 - j] != nums2[-1 - j]:
                break
        return len(nums) - i - j
