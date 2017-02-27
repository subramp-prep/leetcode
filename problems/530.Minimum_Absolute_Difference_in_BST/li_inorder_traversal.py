# coding=utf-8
# Author: Jianghan LI
# Question: 530.Minimum_Absolute_Difference_in_BST/li_inorder_traversal.py
# Date: 27/02/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        l = []

        def bfs(node):
            if node.left:
                bfs(node.left)
            l.append(node.val)
            if node.right:
                bfs(node.right)
        bfs(root)
        return min([abs(l[i] - l[i + 1]) for i in range(len(l) - 1)])
