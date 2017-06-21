# coding=utf-8
# Author: Jianghan LI
# Question: 109.Convert_Sorted_List_to_Binary_Search_Tree
# Date: 2017-06-21
# Complexity: O(N)


class Solution(object):

    def sortedListToBST(self, head):
        self.head, n = head, 0
        while head:
            head, n = head.next, n + 1
        return self.helper(n)

    def helper(self, n):
        if not n:
            return None
        left = self.helper(n >> 1)
        root, self.head = TreeNode(self.head.val), self.head.next
        root.left, root.right = left, self.helper((n - 1) >> 1)
        return root
