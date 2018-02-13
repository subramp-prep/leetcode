# coding=utf-8
# Author: Jianghan LI
# Question: 750.Number_Of_Corner_Rectangles
# Complexity: O(N)
# Date: 2017-12-17 0:19:42 - 0:28:07, 0 wrong try

import itertools
import collections


class Solution(object):

    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        d = {}
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for i in range(n):
                if grid[x][i]:
                    for j in range(i + 1, n):
                        if grid[x][j]:
                            d[(i, j)] = d.get((i, j), 0) + 1
        return sum(d[i] * (d[i] - 1) / 2 for i in d)

    # combinations
    def countCornerRectangles(self, grid):
        d, n = {}, len(grid[0])
        for line in grid:
            for i, j in itertools.combinations([i for i in range(n) if line[i]], 2):
                d[i, j] = d.get((i, j), 0) + 1
        return sum(x * (x - 1) / 2 for x in d.values())

    # combinations + Counter
    def countCornerRectangles(self, grid):
        d = collections.Counter(ij for line in grid
                                for ij in itertools.combinations((i for i, v in enumerate(line) if v), 2))
        return sum(x * (x - 1) / 2 for x in d.values())

    def countCornerRectangles(self, grid):
        n = len(grid[0])
        d = collections.Counter((i, j) for line in grid for i in range(n)
                                for j in range(i + 1, n) if line[i] and line[j])
        return sum(x * (x - 1) / 2 for x in d.values())

    def countCornerRectangles(self, grid):
        d = collections.Counter((i, j) for line in grid
                                for j in range(len(line)) if line[j]
                                for i in range(j) if line[i])
        return sum(x * (x - 1) / 2 for x in d.values())

############ test case ###########
s = Solution()
print s.countCornerRectangles([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])  # 9
print s.countCornerRectangles([[1, 0, 0, 1, 0],
                               [0, 0, 1, 0, 1],
                               [0, 0, 0, 1, 0],
                               [1, 0, 1, 0, 1]])  # 1
print s.countCornerRectangles([[1, 1, 1, 1]])  # 0

############ comments ############

# https://discuss.leetcode.com/topic/114335/python-solution
