# coding=utf-8
# Author: Jianghan LI
# Question: 305.Number_of_Islands_II
# Complexity: O(N)
# Date: 2018-05 16:28 - 16:44
class Solution(object):

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m * n == 0:
            return 0
        parents = {}
        self.count = 0
        def add(x):
            if x not in parents:
                parents[x] = x
                self.count += 1
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1

        res = []
        for x, y in positions:
            add((x, y))
            if x > 0 and (x - 1, y) in parents:
                union((x, y), (x - 1, y))
            if y > 0 and (x, y - 1) in parents:
                union((x, y), (x, y - 1))
            if x < m - 1 and (x + 1, y) in parents:
                union((x, y), (x + 1, y))
            if y < n - 1 and (x, y + 1) in parents:
                union((x, y), (x, y + 1))
            res.append(self.count)
            # print parents
        return res


############ test case ###########
s = Solution()
# print s.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]])  # [1, 1, 2, 3]
print s.numIslands2(m=3, n=6, positions=[[2, 2], [2, 1], [1, 3], [0, 4]])  # [1, 1, 2, 3]
print s.numIslands2(8, 4, [[0, 0], [7, 1], [6, 1], [3, 3], [4, 1]])  # [1,2,2,3,4]


############ comments ############
# 1 wrong try for key problems: use 2d key
# 1 wrong try for count O(MN): use O(1) count
