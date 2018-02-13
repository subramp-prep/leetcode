# coding=utf-8
# Author: Jianghan LI
# Question: 783.Minimum_Distance_Between_BST_Nodes
# Complexity: O(N) O(1)
# Date: 2018-02-11  0:00:00 - 0:09:06, 0 wrong try


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        bfs = [root]
        for i in bfs:
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        bfs = sorted(i.val for i in bfs)
        return min(b - a for a, b in zip(bfs, bfs[1:]))
