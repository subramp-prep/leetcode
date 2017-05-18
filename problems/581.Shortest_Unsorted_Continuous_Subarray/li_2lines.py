# coding=utf-8
# Author: Jianghan LI
# Question: 581.Shortest_Unsorted_Continuous_Subarray
# Date: 2017-05-17
# Complexity: O(NlogN)


class Solution(object):

    def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
