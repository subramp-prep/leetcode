# coding=utf-8
# Author: Jianghan LI
# Question: 671.Second_Minimum_Node_In_a_Binary_Tree
# Complexity: O(N)
# Date: 2017-09－03
# Contest48 0:00:00 - 0:05:47, 0 wrong try



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        def dfs(root):
            if not root: return []
            res = dfs(root.left) + dfs(root.right) + [root.val]
            return sorted(list(set(res)))[:2]

        res = dfs(root)
        return res[1] if len(res) == 2 else -1

