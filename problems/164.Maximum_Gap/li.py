# coding=utf-8
# Author: Jianghan LI
# Question: 164.Maximum_Gap
# Date: 2017-04-09 11:01 - 11:01
# Complexity: O(NlogN)


class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(y - x for x, y in zip(nums, nums[1:])) if len(nums) > 1 else 0

    def maximumGap2(self, nums):
        nums = sorted(collections.Counter(nums).keys())
        return max(y - x for x, y in zip(nums, nums[1:])) if len(nums) > 1 else 0
