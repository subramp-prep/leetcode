# coding=utf-8
# Author: Jianghan LI
# Question: 230.Kth_Smallest_Element_in_a_BST
# Complexity: O(N)
# Date: 2017-10-03


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # iteration
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        inorder = []
        cur = root
        while k:
            while cur:
                inorder.append(cur)
                cur = cur.left
            cur = inorder.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

    # recursion
    def kthSmallest(self, root, k):
        self.k = k

        def find(root):
            if root:
                x = find(root.left)
                if not self.k:
                    return x
                self.k -= 1
                if not self.k:
                    return root.val
                return find(root.right)
        return find(root)
