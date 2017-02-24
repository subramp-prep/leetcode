# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-04 11:51-12:06


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findFrequentTreeSum(self, root):
        if root == None:
            return []

        def getSum(node):
            if node == None:
                return 0
            s = node.val + getSum(node.left) + getSum(node.right)
            c[s] += 1
            return s

        from collections import Counter
        c = Counter()
        getSum(root)
        frequent = max(c.values())  # calculate this line fisrtly
        return [s for s in c.keys() if c[s] == frequent]


s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print s.findFrequentTreeSum(root)


# I have used a hash-map ctr to count the sum occurrence.

# I have wrote a sub function countSubtreeSum to travel through a tree and
# return the sum of the tree.

# In countSubtreeSum, I will travel through the left node and the right node,
# calculate the sum of the tree, increment the counter ctr, and return the sum.

# https://discuss.leetcode.com/topic/77769/python-easy-understand-solution
