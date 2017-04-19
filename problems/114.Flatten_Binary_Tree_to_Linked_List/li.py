# coding=utf-8
# Author: Jianghan LI
# Question: 114.Flatten_Binary_Tree_to_Linked_List
# Date: 2017-04-19 9:15 - 9:21

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        queue = [root]
        if root.right:
            queue.append(root.right)
        if root.left:
            queue.append(root.left)
        while queue:
            cur = queue.pop()
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
            root.right = cur
            root.left = None
            root = cur
        root.right = None
