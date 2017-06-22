# coding=utf-8
# Author: Jianghan LI
# Question: 109.Convert_Sorted_List_to_Binary_Search_Tree
# Date: 2017-06-21 09:06 - 09:18, 1 wrong try
# Complexity: O(NlogN)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        cur = head
        for i in range(n / 2 - 1):
            cur = cur.next
        mid = cur.next
        cur.next = None
        right = mid.next
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root
