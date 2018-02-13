# coding=utf-8
# Author: Jianghan LI
# Question: 773.Sliding_Puzzle
# Date: 2018-01-28, 0:17:43 - 0:51:19, 1 wrong try


class Solution(object):

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.memo = dict()
        order = tuple(board[0] + board[1])
        count = 0
        for i in range(6):
            for j in range(i + 1, 6):
                if order[i] > order[j] > 0:
                    count += 1
        if count % 2:
            return -1
        bfs = [(order, 0)]
        for m, steps in bfs:
            if m == (1, 2, 3, 4, 5, 0):
                return steps
            for i in range(6):
                if m[i] == 0:
                    self.add(bfs, m, i, (i + 3) % 6, steps + 1)
                    if i % 3 != 2:
                        self.add(bfs, m, i, i + 1, steps + 1)
                    if i % 3 != 0:
                        self.add(bfs, m, i, i - 1, steps + 1)

    def swap(self, m, i, j):
        l = list(m)
        l[i], l[j] = l[j], l[i]
        return tuple(l)

    def add(self, bfs, m, i, j, steps):
        nt = (self.swap(m, i, j), steps)
        if nt not in self.memo:
            bfs.append(nt)
            self.memo[nt] = steps


############ test case ###########
s = Solution()

print s.slidingPuzzle([[1, 2, 3], [5, 4, 0]])  # -1
print s.slidingPuzzle([[4, 1, 2], [5, 0, 3]])  # 5

print s.slidingPuzzle([[3, 0, 1], [2, 4, 5]])  # 5


############ comments ############
