# coding=utf-8
# Author: Jianghan LI
# Question: 226.Invert_Binary_Tree
# Complexity: O(N)
# Date: 2017-07-04 9:17 - 9:20

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
