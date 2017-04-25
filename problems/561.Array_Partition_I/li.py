# coding=utf-8
# Author: Jianghan LI
# Question: 561.Array_Partition_I
# Date: 2017-04-24 10:16 - 10:16


class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
