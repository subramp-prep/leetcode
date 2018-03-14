# coding=utf-8
# Author: Jianghan LI
# Question: 797.All_Paths_From_Source_to_Target
# Date: 2018-03-10 0:04:53 - 0:09:07, 0 wrong try


class Solution(object):

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res

    # recursion
    def allPathsSourceTarget(self, g, cur=0):
        if cur == len(g) - 1:
            return [[len(g) - 1]]
        res = []
        for i in g[cur]:
            for path in self.allPathsSourceTarget(g, i):
                res.append([cur] + path)
        return res

    # recursion 2-line
    def allPathsSourceTarget(self, g, cur=0):
        if cur == len(g) - 1:
            return [[len(g) - 1]]
        return [([cur] + path) for i in g[cur] for path in self.allPathsSourceTarget(g, i)]

############ test case ###########
s = Solution()
print s.allPathsSourceTarget([[1, 2], [3], [3], []])

############ comments ############
