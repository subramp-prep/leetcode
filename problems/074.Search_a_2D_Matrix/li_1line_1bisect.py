# coding=utf-8
# Author: Jianghan Li
# Question: 74. Search a 2D Matrix
# Date: 15/03/2017


class Solution(object):

    def searchMatrix(self, matrix, target):
        return bool(matrix) and target in matrix[bisect.bisect(matrix, [target + 0.5]) - 1] and target in matrix[bisect.bisect(matrix, [target + 0.5]) - 1]

# https://discuss.leetcode.com/topic/16543/6-12-lines-o-log-m-log-n-myself-library/6
