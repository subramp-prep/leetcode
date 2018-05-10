# coding=utf-8
# Author: Jianghan LI
# Question: 261.Graph_Valid_Tree
# Complexity: O(N)
# 2018-05 10:42 - 10:59, 1 wrong try

import collections
class Solution(object):

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        connect = collections.defaultdict(set)
        for a, b in edges:
            connect[a].add(b)
            connect[b].add(a)
        seen = set([0])
        bfs = [[-1, 0]]
        for a, b in bfs:
            for c in connect[b]:
                if c == a:
                    continue
                if c in seen:
                    return False
                seen.add(c)
                bfs.append((b, c))
        return len(seen) == n

    def validTree(self, n, edges):
        connect = collections.defaultdict(set)
        for a, b in edges:
            connect[a].add(b)
            connect[b].add(a)
        seen = set([0])
        bfs = [0]
        for i in bfs:
            for j in connect[i]:
                if j not in seen:
                    seen.add(j)
                    bfs.append(j)
        return len(seen) == n and len(edges) == n - 1


############ test case ###########
s = Solution()
print s.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
print s.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])  # false.


############ comments ############
# 1 wrong try: not seen all node.
# BFS, len(seen) = n and 每个node遇见一次
# BFS, len(seen) = n and len(edges) == n - 1
