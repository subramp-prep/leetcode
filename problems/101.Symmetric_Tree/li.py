# coding=utf-8
# Author: Jianghan LI
# Question: 101.Symmetric_Tree
# Date: 2017-04-12 09:46 -09:59
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
