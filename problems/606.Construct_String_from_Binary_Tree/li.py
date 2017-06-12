# coding=utf-8
# Author: Jianghan LI
# Question: 606.Construct_String_from_Binary_Tree
# Date: 2017-06-06 17:19 - 17:28， 0 wrong try
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        left, right = self.tree2str(t.left), self.tree2str(t.right)
        if right:
            return "%s(%s)(%s)" % (t.val, left, right)
        if left:
            return "%s(%s)" % (t.val, left)
        return "%s" % t.val

    # shorter
    def tree2str(self, t):
        if not t:
            return ""
        left, right = self.tree2str(t.left), self.tree2str(t.right)
        return "%s(%s)(%s)" % (t.val, left, right) if right else "%s(%s)" % (t.val, left) if left else "%s" % t.val
