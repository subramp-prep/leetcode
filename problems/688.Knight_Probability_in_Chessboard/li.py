# coding=utf-8
# Author: Jianghan LI
# Question: 688.Knight_Probability_in_Chessboard
# Complexity: O(KN^2)
# Date: 2017-10-01 10:19 - 10:27, 0 wrong try


class Solution(object):

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        board = [[0] * N for i in range(N)]
        board[r][c] = 1
        for _ in range(K):
            board2 = [[0] * N for i in range(N)]
            for x in range(N):
                for y in range(N):
                    for i, j in [[-1, -2], [1, -2], [-1, 2], [1, 2], [-2, -1], [2, -1], [-2, 1], [2, 1]]:
                        if 0 <= x + i < N and 0 <= y + j < N:
                            board2[x + i][y + j] += board[x][y]
            board = board2
        return sum(i for row in board for i in row) / float(8 ** K)
