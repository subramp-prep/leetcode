import collections


class Solution(object):

    def movesToChessboard(self, b):
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)):
            return -1
        if not N / 2 <= sum(b[0]) <= (N + 1) / 2:
            return -1
        if not N / 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) / 2:
            return -1
        col = sum(b[0][i] == i % 2 for i in range(N))
        row = sum(b[i][0] == i % 2 for i in range(N))
        if N % 2:
            if col % 2:
                col = [col, N - col][col % 2]
            if row % 2:
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


# if len(set(map(tuple, b))) != 2: return -1
# if len(set(map(tuple, zip(*b)))) != 2: return -1
# the same as:
# if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)):
# return -1


# Two conditions to help solve this problem:

# In a valid chess board, there are 2 and only 2 kinds of rows and one is inverse to the other.
# For example if there is a row 01010011 in the board, any other row must be either 01010011 or 10101100.
# The same for columns
# A corollary is that, any rectangle inside the board with corners top
# left, top right, bottom left, bottom right must be 4 zeros or 2 ones 2
# zeros or 4 zeros.

# Another important property is that every row and column has half ones. Assume the board is N * N:
# If N = 2*K, every row and every column has K ones and K zeros.
# If N = 2*K + 1, every row and every column has K ones and K + 1 zeros or K + 1 ones and K zeros.

# Since the swap process does not break this property, for a given board to be valid, this property must hold.
# These two conditions are necessary and sufficient condition for a valid chessboard.

# Once we know it is a valid cheese board, we start to count swaps.
# Basic on the property above, when we arange the first row, we are actually moving all columns.

# I try to arrange one row into 01010 and 10101 and I count the number of swaps.

# In case of N even, I take the minimum swaps, because both are possible.
# In case of N odd, I take the even swaps.
# Because when we make a swap, we move 2 columns or 2 rows at the same time.
# So col swaps and row swaps should be even here.
