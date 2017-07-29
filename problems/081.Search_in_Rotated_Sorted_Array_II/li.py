# coding=utf-8
# Author: Jianghan LI
# Question: 081.Search_in_Rotated_Sorted_Array_II
# Complexity: O(N)
# Date: 2017-07-07 9:21 - 9:21


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return target in set(nums)
