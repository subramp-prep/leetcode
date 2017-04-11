# coding=utf-8
# Author: Jianghan LI
# Question: 542.01_Matrix
# Date: 2017-04-11
# Complexity: O(N)


class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        N, M = len(matrix), len(matrix[0])
        res = [[10000 * matrix[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                res[i][j] = min(res[i][j], res[i - 1][j] + 1 if i else 10000,
                                res[i][j - 1] + 1 if j else 10000)
        for i in range(N):
            for j in range(M - 1, -1, -1):
                res[i][j] = min(res[i][j], res[i - 1][j] + 1 if i else 10000,
                                res[i][j + 1] + 1 if j < M - 1 else 10000)
        for i in range(N - 1, -1, -1):
            for j in range(M):
                res[i][j] = min(res[i][j], res[i + 1][j] + 1 if i < N -
                                1 else 10000, res[i][j - 1] + 1 if j else 10000)
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                res[i][j] = min(res[i][j], res[i + 1][j] + 1 if i < N - 1 else 10000,
                                res[i][j + 1] + 1 if j < M - 1 else 10000)
        return res

    def updateMatrix2(self, matrix):
        N, M = len(matrix), len(matrix[0])
        res = [[10000 * x for x in row] for row in matrix]
        for i in range(N):
            for j in range(M):
                res[i][j] = min(res[i][j], res[i - 1][j] + 1 if i else 10000,
                                res[i][j - 1] + 1 if j else 10000)
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                res[i][j] = min(res[i][j], res[i + 1][j] + 1 if i < N - 1 else 10000,
                                res[i][j + 1] + 1 if j < M - 1 else 10000)
        return res

# DP的思路，左上到右下，然后扫四个方向
# 后来发现，需要的四个方向其实是上下左右，左上到右下满足了向下和向右的方向，只需要再右下到左上就可以了。
