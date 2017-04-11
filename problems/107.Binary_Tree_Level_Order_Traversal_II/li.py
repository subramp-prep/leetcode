# coding=utf-8
# Author: Jianghan LI
# Question: 107.Binary_Tree_Level_Order_Traversal_II
# Date: 2017-04-10 15:27 - 15:35

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root]]
        while 1:
            children = []
            for i in range(len(res[-1])):
                if res[-1][i].left:
                    children.append(res[-1][i].left)
                if res[-1][i].right:
                    children.append(res[-1][i].right)
                res[-1][i] = res[-1][i].val
            if children:
                res.append(children)
            else:
                break
        return res[::-1]
