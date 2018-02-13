# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.inorder(root.right)


# no helper
class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res


############ comments ############
# https://discuss.leetcode.com/topic/120339
