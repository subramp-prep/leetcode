# coding=utf-8
# Author: Jianghan LI
# Question: 515.Find_Largest_Value_in_Each_Tree_Row
# Date: 2017-04-13 10:29 - 10:34

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None``


class Solution(object):

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue, res = [root], []
        while queue:
            res.append(max(node.val for node in queue))
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res
