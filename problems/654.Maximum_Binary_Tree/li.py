# coding=utf-8
# Author: Jianghan LI
# Question: 1
# Complexity: O(N)
# Date: 2017-08-06


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        v = max(nums)
        root = TreeNode(v)
        i = nums.index(v)
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return root

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        root, maxi = TreeNode(max(nums)), nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxi])
        root.right = self.constructMaximumBinaryTree(nums[maxi + 1:])
        return root
