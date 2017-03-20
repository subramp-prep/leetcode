# coding=utf-8
# Author: Jianghan LI
# Question: 240.Search_a_2D_Matrix_II
# Date: 2017-03-15 23:54
# Complexity: O(N) O(N)

import bisect


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not any(matrix):
            return False
        j = len(matrix[0])
        for i in range(len(matrix)):
            j = bisect.bisect(matrix[i], target, 0, j)
            if j > 0:
                if matrix[i][j - 1] == target:
                    return True
            else:
                return False
        return False


s = Solution()
print s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)

# 从右上角开始查找，比target大左移，比target小下移。
# 每行内使用bisect查找左移到的位置。
# 性能一般，复杂度mlogn
