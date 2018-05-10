# coding=utf-8
# Author: Jianghan LI
# Question: 684.Redundant-Connection
# Complexity: O(N)
# Date: 2018-05 16:58 - 17:02

class Solution(object):

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
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
                return True
            return False
        ## main ##
        for x, y in edges:
            add(x)
            add(y)
            if not union(x, y):
                return [x, y]


############ test case ###########
s = Solution()
print s.findRedundantConnection([[1, 2], [1, 3], [2, 3]])  # [2, 3]
print s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])  # [1, 4]
