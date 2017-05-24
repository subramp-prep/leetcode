# coding=utf-8
# Author: Jianghan LI
# Question: 144.Binary_Tree_Preorder_Traversal
# Complexity: O(N)


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else return []

# Date: 2017-05-20 10:24 － 10:27
# 1 wrong try: preorder, not inorder
