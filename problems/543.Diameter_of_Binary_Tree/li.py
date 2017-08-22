# coding=utf-8
# Author: Jianghan LI
# Question: 543.Diameter_of_Binary_Tree
# Complexity: O(N)
# Date: 2017-07-30 13:12 - 13:18, 0 wrong try

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.ret = max(self.ret, left + right)
            return max(left, right) + 1
        self.ret = 0
        depth(root)
        return self.ret
