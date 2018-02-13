# coding=utf-8
# Author: Jianghan LI
# Question: 766.Toeplitz_Matrix
# Complexity: O(MN)
# Date: 2018-01-21 0:10:16 － 0:22:08, 0 wrong try


class Solution(object):

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        m, n = len(matrix), len(matrix[0])
        res = [set() for _ in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                res[i - j].add(matrix[i][j])
        return all(len(s) == 1 for s in res)

    def isToeplitzMatrix(self, matrix):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True

    def isToeplitzMatrix(self, m):
        return all(m[i][j] == m[i + 1][j + 1] for i in range(len(m) - 1) for j in range(len(m[0]) - 1))

############ test case ###########
s = Solution()
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]  # True
matrix = [[1, 2], [2, 2]]  # False
print s.isToeplitzMatrix(matrix)
print s.isToeplitzMatrix([[]])

############ comments ############
