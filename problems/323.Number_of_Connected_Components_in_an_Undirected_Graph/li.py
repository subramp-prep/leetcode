# coding=utf-8
# Author: Jianghan LI
# Question: 323.Number_of_Connected_Components_in_an_Undirected_Graph
# Complexity: O(N)
# Date: 2018-05 16:00 - 16:07, 0 wrong try
class Solution(object):

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = range(n)
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(xy):
            x, y = xy
            x, y = find(x), find(y)
            parents[x] = y
        def count():
            return sum(x == parents[x] for x in range(n))

        map(union, edges)
        return count()

############ test case ###########
s = Solution()
print s.countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]])
