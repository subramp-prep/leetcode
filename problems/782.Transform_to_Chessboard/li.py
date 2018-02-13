# coding=utf-8
# Author: Jianghan LI
# Question: 782.Transform_to_Chessboard
# Complexity: O(N^2)
# Date: 2018-02-11 0:20:10 - 1:16:27, 3 wrong tries

import collections


class Solution(object):

    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        def checkeven():
            s = collections.Counter(tuple(l) for l in board)
            if len(s) != 2:
                return -1
            for i in s:
                if sum(i) != N / 2 or s[i] != N / 2:
                    return -1
            for a, b in zip(*s.keys()):
                if a == b:
                    return -1
            res1 = 0
            for i in range(N):
                if board[0][i] != i & 1:
                    res1 += 1
            res1 = min(N - res1, res1)
            res2 = 0
            for i in range(N):
                if board[i][0] != i & 1:
                    res2 += 1
            res2 = min(N - res2, res2)
            return (res1 + res2) / 2

        def checkodd():
            s = collections.Counter(tuple(l) for l in board)
            if len(s) != 2:
                return -1
            for i in s:
                if sum(i) not in [N / 2, N / 2 + 1] or s[i] not in [N / 2, N / 2 + 1]:
                    return -1
            for a, b in zip(*s.keys()):
                if a == b:
                    return -1
            line1, line2 = s.keys()
            if s[line1] < s[line2]:
                line1, lin2 = line2, line1

            res1 = 0
            for i in range(N):
                if board[0][i] != i & 1:
                    res1 += 1
            if res1 & 1:
                res1 = N - res1
            res2 = 0
            for i in range(N):
                if board[i][0] != i & 1:
                    res2 += 1
            if res2 & 1:
                res2 = N - res2
            return (res1 + res2) / 2

        if N & 1:
            return checkodd()
        else:
            return checkeven()


############ test case ###########
s = Solution()
print s.movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]])  # 2
print s.movesToChessboard([[1, 0], [0, 1]])  # 0
print s.movesToChessboard([[1, 0], [1, 0]])  # -1

print s.movesToChessboard([[1, 1, 0], [0, 0, 1], [0, 0, 1]])  # 2
print s.movesToChessboard([[0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 0]])  # 2


############ comments ############
