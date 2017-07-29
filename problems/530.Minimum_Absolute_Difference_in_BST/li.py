# coding=utf-8
# Author: Jianghan LI
# Question: 530.Minimum_Absolute_Difference_in_BST/li.py
# Date: 27/02/2017
# Date: 2017-05-17 09:12 - 09:19

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        def dfs(node, l=[]):
            if node.left:
                dfs(node.left, l)
            l.append(node.val)
            if node.right:
                dfs(node.right, l)
            return l
        l = dfs(root)
        return min([abs(a - b) for a, b in zip(l, l[1:])])

    def getMinimumDifference(self, root):
        l = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            l.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(l, l[1:]))

# https://discuss.leetcode.com/topic/81017/python-7-lines-ac-solution-with-comments
# I am not sure if I well understand the question. I simply read all value in a list land sort it.
# Note: There are at least two nodes in this BST.
