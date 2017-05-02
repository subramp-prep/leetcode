# coding=utf-8
# Author: Jianghan LI
# Question: 566.Reshape_the_Matrix
# Date: 2017-05-02


class Solution(object):

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        return [l[i * c: i * c + c] for i in xrange(r)] if r * c == len(l) else nums
