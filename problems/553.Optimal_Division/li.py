# coding=utf-8
# Author: Jianghan LI
# Question: 553.Optimal_Division
# Date: 2017-04-18 13:45 - 13:53


class Solution(object):

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] + "/" + nums[1]
        return nums[0] + "/(" + "/".join(nums[1:]) + ")"
