# coding=utf-8
# Author: Jianghan LI
# Question: 450.Delete_Node_in_a_BST
# Complexity: O(logN)
# Date: 2017-09-27


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.right:
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right
        else:
            return root.left
        return root


# 没有delete key点
# 修改了树的高度
# 简便方法 始终有问题
