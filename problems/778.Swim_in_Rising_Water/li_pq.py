# coding=utf-8
# Author: Jianghan LI
# Question: 778.Swim_in_Rising_Water
# Complexity: O(N)
# Date: 2018-02-09

import heapq


class Solution(object):

    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))


############ test case ###########
s = Solution()
print s.swimInWater([[0, 1, 2, 3, 4],
                     [24, 23, 22, 21, 5],
                     [12, 13, 14, 15, 16],
                     [11, 17, 18, 19, 20],
                     [10, 9, 8, 7, 6]])  # 11

print s.swimInWater([[11, 15, 3, 2],
                     [6, 4, 0, 13],
                     [5, 8, 9, 10],
                     [1, 14, 12, 7]])  # 16
