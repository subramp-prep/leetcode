# coding=utf-8
# Author: Jianghan LI
# Question: 662.Maximum_Width_of_Binary_Tree
# Complexity: O(N)
# Date: 2017-09-18 3:03 - 3:12, 0 wrong try


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [(root, 1)]
        res = 0
        while nodes:
            res = max(res, nodes[-1][1] - nodes[0][1] + 1)
            nodes = [i for node, pos in nodes
                     for i in [(node.left, pos * 2), (node.right, pos * 2 + 1)]
                     if i[0]]
        return res
