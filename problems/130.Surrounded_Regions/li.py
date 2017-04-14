# coding=utf-8
# Author: Jianghan LI
# Question: 130.Surrounded_Regions
# Date: 2017-04-14 09:58 - 10:20


class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # board = map(list, board)
        if not any(board):
            return
        M, N = len(board), len(board[0])
        seto = set([])
        queue = []
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    seto.add((i, j))
                    if i == 0 or j == 0 or i == M - 1 or j == N - 1:
                        queue.append((i, j))
        for i, j in queue:
            if 0 <= i < M and 0 <= j < N and board[i][j] == 'X':
                board[i][j] = 'O'
                for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (i2, j2) in seto:
                        queue.append((i2, j2))
        # return board

############ test case ###########
s = Solution()
print s.solve(["OOO", "OXO", "OOO"])

############ comments ############
