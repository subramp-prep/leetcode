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

    def searchMatrix2(self, matrix, target):
        m = bisect.bisect(matrix, [target + 0.5])
        if m:
            n = bisect.bisect(matrix[m - 1], target)
            return len(matrix[0]) > 0 and matrix[m - 1][n - 1] == target
        return False

    def searchMatrix3(self, matrix, target):
        m = bisect.bisect(matrix, [target + 0.5])
        return len(matrix[0]) > 0 and matrix[m - 1][bisect.bisect(matrix[m - 1], target) - 1] == target if m else False


# 两次bisect
# ＋0.5 是为了保证出现在想要找的index后面。
