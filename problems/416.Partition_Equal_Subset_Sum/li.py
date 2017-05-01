# coding=utf-8
# Author: Jianghan LI
# Question: 416.Partition_Equal_Subset_Sum
# Date: 2017-04-29 2:02 - 2:07


class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
        return False

    def canPartition(self, nums):
        return (sum(nums) / 2.) in reduce(lambda cur, x: cur | {v + x for v in cur}, nums, {0})

# https://discuss.leetcode.com/topic/64124/4-line-passed-python-solution/2
