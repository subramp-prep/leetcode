# coding=utf-8
# Author: Jianghan LI
# Question: 200.Number_of_Islands
# Complexity: O(N)
# Date: 2018-05 16:14 - 16:25
class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid):
            return 0
        m, n = len(grid), len(grid[0])
        parents = {}
        def add(x):
            if x not in parents:
                parents[x] = x
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            parents[x] = y
        def count():
            return sum(x == parents[x] for x in parents)

        for i in range(m * n):
            x, y = i / n, i % n
            if grid[x][y] == '1':
                add(i)
                if y > 0 and grid[x][y - 1] == '1':
                    union(i, i - 1)
                if x > 0 and grid[x - 1][y] == '1':
                    union(i, i - n)
        return count()

############ test case ###########
s = Solution()
# print s.numIslands([["1", "1", "1", "1", "0"],
#                     ["1", "1", "0", "1", "0"],
#                     ["1", "1", "0", "0", "0"],
#                     ["0", "0", "0", "0", "0"]])
print s.numIslands(["11000",
                    "11000",
                    "00100",
                    "00011"])
