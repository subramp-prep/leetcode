# coding=utf-8
# Author: Jianghan LI
# Question: 617.Merge_Two_Binary_Trees
# Complexity: O(N)
# Date: 2017-06-12 10:52 - 10:54, 0 wrong try


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # merge t2 into t1 if t1 exists. oterwise return t2

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    # return a new tree. better and shorter
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        res = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        res.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        res.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return res
