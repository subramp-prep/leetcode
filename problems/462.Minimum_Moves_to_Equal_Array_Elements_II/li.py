# coding=utf-8
# Author: Jianghan LI
# Question: 462.Minimum_Moves_to_Equal_Array_Elements_II
# Complexity: O(NlogN)
# Date: 2018-01-10


class Solution(object):

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = sorted(nums)[len(nums) / 2]
        return sum(abs(i - m) for i in nums)
