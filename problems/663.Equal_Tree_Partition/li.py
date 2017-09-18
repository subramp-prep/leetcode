# coding=utf-8
# Author: Jianghan LI
# Question: 663.Equal_Tree_Partition
# Complexity: O(N)
# Date: 2017-08-20
# Contest 46, 0:36:46 - 0:57:02, 2 wrong tries



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def treeSum(root):
            if not root: return 0
            root.val += (root.left and treeSum(root.left) or 0) + (root.right and treeSum(root.right) or 0)
            return root.val
        tree = treeSum(root)
        if tree%2==1: return False

        def findSum(root, s):
            if not root: return False
            if root.val == s: return True
            if root.left and findSum(root.left, s): return True
            if root.right and findSum(root.right, s): return True
            return False

        if not root: return False
        if root.left and findSum(root.left, tree/2): return True
        if root.right and findSum(root.right, tree/2): return True
        return False

