import collections


class Solution(object):

    def movesToChessboard(self, board):
        N = len(board)
        s = collections.Counter(tuple(l) for l in board)
        if len(s) != 2:
            return -1
        for a, b in zip(*s.keys()):
            if a == b:
                return -1
        for i in s:
            if sum(i) not in [N / 2, N / 2 + 1] or s[i] not in [N / 2, N / 2 + 1]:
                return -1
        col = sum(board[0][i] == i & 1 for i in range(N))
        row = sum(board[i][0] == i & 1 for i in range(N))
        if N & 1:
            if col & 1:
                col = N - col
            if row & 1:
                row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) / 2

    def movesToChessboard(self, b):
        N = len(b)
        if len(set(map(tuple, b))) != 2:
            return -1
        if len(set(map(tuple, zip(*b)))) != 2:
            return -1
        if not N / 2 <= sum(b[0]) <= N / 2 + N % 2:
            return -1
        if not N / 2 <= sum(b[i][0] for i in range(N)) <= N / 2 + N % 2:
            return -1

        col = sum(b[0][i] == i & 1 for i in range(N))
        row = sum(b[i][0] == i & 1 for i in range(N))
        if N & 1:
            if col & 1:
                col = N - col
            if row & 1:
                row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) / 2

    def movesToChessboard(self, b):
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)):
            return -1
        if sum(b[0]) not in [N / 2, N / 2 + 1]:
            return -1
        if sum(b[i][0] for i in range(N)) not in [N / 2, N / 2 + 1]:
            return -1
        col = sum(b[0][i] == i & 1 for i in range(N))
        row = sum(b[i][0] == i & 1 for i in range(N))
        if N & 1:
            if col & 1:
                col = N - col
            if row & 1:
                row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) / 2


############ test case ###########
s = Solution()
print s.movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]])  # 2
print s.movesToChessboard([[1, 0], [0, 1]])  # 0
print s.movesToChessboard([[1, 0], [1, 0]])  # -1

print s.movesToChessboard([[1, 1, 0], [0, 0, 1], [0, 0, 1]])  # 2


# https://discuss.leetcode.com/topic/120358/python-solution
