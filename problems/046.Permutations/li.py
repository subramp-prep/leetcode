# coding=utf-8
# Author: Jianghan LI
# Question: 046.Permutations
# Date: 2017-03-25


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
