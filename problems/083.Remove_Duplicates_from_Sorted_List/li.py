# coding=utf-8
# Author: Jianghan LI
# Question: 083.Remove_Duplicates_from_Sorted_List
# Date: 2017-06-22 9:02 - 9:05
# Complexity: O(N)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

    # another
    def deleteDuplicates(self, head):
        if not head:
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
