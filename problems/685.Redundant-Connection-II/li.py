# coding=utf-8
# Author: Jianghan LI
# Question: 685.Redundant-Connection-II
# Complexity: O(N)
# Date: 2018-05 17:06 - 17:49
class Solution(object):

    def findRedundantDirectedConnection(self, edges):
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
                parents[y] = x
                self.count -= 1
                return True
            return False
        ## main ##
        p = {}
        res = []
        for x, y in edges:
            if y not in p:
                p[y] = x
            else:
                res.append([p[y], y])
                res.append([x, y])
                break
        for x, y in edges:
            if res and [x, y] == res[1]:
                continue
            add(x)
            add(y)
            if not union(x, y):
                return res[0] if res else [x, y]
        return res[1]


############ test case ###########
s = Solution()
print s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]])  # [2, 3]
print s.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]])  # [4,1]
print s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]])  # [2, 1]
