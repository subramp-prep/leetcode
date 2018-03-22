# coding=utf-8
# Author: Jianghan LI
# Question: 802.Find_Eventual_Safe_States
# Complexity: O(edges)
# Date: 2018-03-20


class Solution(object):

    def eventualSafeNodes(self, graph):
        safe, unsafe = set(), set()

        def dfs(i):
            if i in safe:
                return True
            if i in unsafe:
                return False
            unsafe.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            safe.add(i)
            unsafe.remove(i)
            return True
        for i in range(len(graph)):
            dfs(i)
        return sorted(safe)

    def eventualSafeNodes(self, graph):
        color = [0] * len(graph)

        def dfs(i):
            if color[i]:
                return color[i] == 2
            color[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            color[i] = 2
            return True
        for i in range(len(graph)):
            dfs(i)
        return [i for i, v in enumerate(color) if v == 2]


############ test case ###########
s = Solution()
print s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []])  # [2,4,5,6]
