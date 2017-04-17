# coding=utf-8
# Author: Jianghan LI
# Question: 098.Validate_Binary_Search_Tree
# Date: 2017-04-17


class Solution:

    def isValidBST(self, root):
        self.res = []
        return self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return True
        if not self.inOrder(root.left):
            return False
        if len(self) and self.res[-1] >= root.val:
            return False
        self.res.append(root.val)
        return self.inOrder(root.right)

# Simple inorder traversal is quite slow..
# Yes, O(n) guaranteed, but do we have chance to "short circuit" as soon as
# we find the incorrect ordering while doing the inOrder().
# So I modified the solution.
# https://discuss.leetcode.com/topic/10455/python-version-based-on-inorder-traversal
