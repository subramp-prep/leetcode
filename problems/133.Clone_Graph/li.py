# coding=utf-8
# Author: Jianghan LI
# Question: 133.Clone_Graph
# Date: 2017-05-10


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        if not node:
            return None
        find = {}
        seen = set()
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur.label in seen:
                continue
            if cur.label not in find:
                find[cur.label] = UndirectedGraphNode(cur.label)
            for i in cur.neighbors:
                if i.label not in find:
                    find[i.label] = UndirectedGraphNode(i.label)
                find[cur.label].neighbors.append(find[i.label])
                stack.append(i)
            seen.add(cur.label)
        return find[node.label]

    def cloneGraph(self, node):
        def getNode(label):
            if label not in nodes:
                nodes[label] = UndirectedGraphNode(label)
            return nodes[label]
        if not node:
            return None
        nodes, seen, stack = {}, set(), [node]
        while stack:
            cur = stack.pop()
            if cur.label in seen:
                continue
            for i in cur.neighbors:
                getNode(cur.label).neighbors.append(getNode(i.label))
                stack.append(i)
            seen.add(cur.label)
        return getNode(node.label)
