# coding=utf-8
# Author: Jianghan LI
# Question: 1
# Complexity: O(N)
# Date: 2017-08-06


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        bfs = [root]
        s = set()
        for i in bfs:
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        for i in s:
            if k - i != i and k - i in s:
                return True
        return False

    def findTarget(self, root, k):
        if not root:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False
