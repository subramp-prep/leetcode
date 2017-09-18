# coding=utf-8
# Author: Jianghan LI
# Question: 453.Minimum_Moves_to_Equal_Array_Elements
# Complexity: O(N)
# Date: 2017-09-15 09:24 - 09:25

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)


#每一步相当于让一个数减1

