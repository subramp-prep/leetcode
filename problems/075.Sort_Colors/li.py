# coding=utf-8
# Author: Jianghan LI
# Question: 075.Sort_Colors
# Date: 2017-05-22 09:08 - 09:08
# Complexity: O(NlogN)


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

# quick sort in place， 0 wrong try
