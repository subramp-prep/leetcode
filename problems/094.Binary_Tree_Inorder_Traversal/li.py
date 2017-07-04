# coding=utf-8
# Author: Jianghan LI
# Question: 094.Binary_Tree_Inorder_Traversal
# Date: 2017-07-03 13:26 - 13:37, 0 wrong try
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # Recursive solution is trivial
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    # iteratively
    def inorderTraversal(self, root):

        stack = []
        ret = []
        cur = root
        while 1:
            while cur:
                stack.append(cur)
                cur = cur.left
            if not stack:
                break
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret

    # a little better, change condition
    def inorderTraversal(self, root):
        stack, ret, cur = [], [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret

# stack replaces recursion stack
# cur replaces recursion input
# ret repalces ruduced return value
