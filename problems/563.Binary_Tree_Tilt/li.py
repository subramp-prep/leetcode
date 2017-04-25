# coding=utf-8
# Author: Jianghan LI
# Question: 563.Binary_Tree_Tilt
# Date: 2017-04-24 9:54 - 10:02

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tilt(root):
            # return (sum, tilt) of tree
            if not root:
                return (0, 0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, abs(left[0] - right[0]) + left[1] + right[1])
        return tilt(root)[1]

# https://discuss.leetcode.com/topic/87398/python-straightforward-solution
# Think about a recursive function. Beside the tilt of subtrees, we also need to get the sum of subtrees.
# So I came up with the idea of sub function tilt(root), which returns the tuple (sum, tilt) of tree
