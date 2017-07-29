# coding=utf-8
# Author: Jianghan LI
# Question: 034.Search_for_a_Range
# Complexity: O(N)
# Date: 2017-07-17 01:40 - 01:44


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [a, b] if a <= b else [-1, -1]

# 2 wrong try, [-1, -1]的返回条件
