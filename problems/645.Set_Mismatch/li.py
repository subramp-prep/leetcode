# coding=utf-8
# Author: Jianghan LI
# Question: 645.Set_Mismatch
# Complexity: O(N)
# Date: 2017-10-22 6:57 - 6:58


class Solution(object):

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {i: 0 for i in range(1, len(nums) + 1)}
        for i in nums:
            d[i] += 1
        return [i for i in d if d[i] == 2] + [i for i in d if d[i] == 0]
