# coding=utf-8
# Author: Jianghan LI
# Question: 098.Validate_Binary_Search_Tree
# Date: 2017-04-17

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def BST_range(root):
            if root.left:
                left_range = BST_range(root.left)
                if left_range and left_range[1] < root.val:
                    left_min = left_range[0]
                else:
                    return False
            else:
                left_min = root.val
            if root.right:
                right_range = BST_range(root.right)
                if right_range and right_range[0] > root.val:
                    right_max = right_range[1]
                else:
                    return False
            else:
                right_max = root.val
            return (left_min, right_max)
        return bool(BST_range(root))
