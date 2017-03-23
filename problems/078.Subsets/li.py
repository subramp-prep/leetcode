# coding=utf-8
# Author: Jianghan LI
# Question: 78. Subsets
# Date: 22/03/2017 11:55 - 11:58
# itertools, beats 90%+


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]
