# coding=utf-8
# Author: Jianghan Li
# Question: 74. Search a 2D Matrix
# Date: 15/03/2017 17:57 - 18:11


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = bisect.bisect(matrix, [target + 0.5])
        if m:
            n = bisect.bisect_left(matrix[m - 1], target)
            if n < len(matrix[m - 1]):
                return matrix[m - 1][n] == target
        return False
