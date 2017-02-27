# coding=utf-8
# Author: Jianghan LI
# Question: 530.Minimum_Absolute_Difference_in_BST/li.py
# Date: 27/02/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        def bfs(node, l=[]):
            l.append(node.val)
            if node.left:
                bfs(node.left, l)
            if node.right:
                bfs(node.right, l)
            return l
        l = sorted(bfs(root))
        return min([abs(l[i] - l[i + 1]) for i in range(len(l) - 1)])


# https://discuss.leetcode.com/topic/81017/python-7-lines-ac-solution-with-comments
# I am not sure if I well understand the question. I simply read all value in a list land sort it.
# Note: There are at least two nodes in this BST.
