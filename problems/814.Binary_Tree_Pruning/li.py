# coding=utf-8
# Author: Jianghan LI
# Question: 814.Binary_Tree_Pruning
# Complexity: O(N)
# Date:2018-04-07 0:10:06 - 0:33:57, 0 wrong try


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root.left: root.left = self.pruneTree(root.left)
        if root.right: root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root

    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left == root.right == None and root.val == 0: return None
        return root

    def pruneTree(self, root):
        if root: root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if root and (root.left or root.right or root.val): return root


############ comments ############

#recursive Solution, very self-explaining
