# coding=utf-8
# Author: Jianghan LI
# Question: 047.Permutations_II
# Date: 2017-03-25 01:00 - 01:02


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(itertools.permutations(nums)))
