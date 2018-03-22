# coding=utf-8
# Author: Jianghan LI
# Question: 802.Find_Eventual_Safe_States
# Complexity: O(edges)
# Date: 2018-03-17 0:29:45 - 0:55:19, 2 wrong tries

import collections


class Solution(object):

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe = set()
        d = {i: set(ends) for i, ends in enumerate(graph)}
        changed = True
        while changed:
            changed = False
            for i in d.keys():
                for j in list(d[i]):
                    if j in safe:
                        d[i].remove(j)
                if not d[i]:
                    changed = True
                    safe.add(i)
                    del d[i]
        return [i for i in range(len(graph)) if i not in d]

    def eventualSafeNodes(self, graph):
        n = len(graph)
        out_degree = [0] * n
        in_nodes = collections.defaultdict(list)
        queue = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                queue.append(i)
            for j in graph[i]:
                in_nodes[j].append(i)
        for term_node in queue:
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    queue.append(in_node)
        return sorted(queue)


############ test case ###########
s = Solution()
print s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []])  # [2,4,5,6]

# 可以不用safe set，因为它是d的补集
# 返回结果也可以用sorted(safe)，但复杂度更高

# 第二个方法因为直接查找父节点，比遍历所有节点要快很多
