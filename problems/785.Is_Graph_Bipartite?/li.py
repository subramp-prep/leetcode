# coding=utf-8
# Author: Jianghan LI
# Question: 785.Is_Graph_Bipartite?
# Complexity: O(N)


class Solution(object):

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
            if not dfs(i):
                return False
        return True


############ test case ###########
s = Solution()
print s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
print s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])


############ comments ############
# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution
