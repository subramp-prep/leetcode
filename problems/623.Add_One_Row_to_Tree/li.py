# coding=utf-8
# Author: Jianghan LI
# Question: 623.Add_One_Row_to_Tree
# Date: 2017-06-19 13:20 - 13:33, 1 wrong try
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            ret, ret.left = TreeNode(v), root
            return ret
        nodes = [root]
        for i in range(d - 2):
            nodes = [i for node in nodes for i in (node.left, node.right) if i]
        for i in nodes:
            i.left, i.left.left = TreeNode(v), i.left
            i.right, i.right.right = TreeNode(v), i.right
        return root

    # better
    def addOneRow(self, root, v, d):
        ret, ret.left = TreeNode(v), root
        row = [ret]
        for _ in range(d - 1):
            row = [i for node in row for i in (node.left, node.right) if i]
        for i in row:
            i.left, i.left.left = TreeNode(v), i.left
            i.right, i.right.right = TreeNode(v), i.right
        return ret.left

# wrong try 1: nodes takes not None.
# wrong try 2: test case d = 1
