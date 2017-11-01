# coding=utf-8
# Author: Jianghan LI
# Question: 141.Linked_List_Cycle
# Complexity: O(N)
# Date: 2017-10-17 02:55 - 02:55

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        return slow == fast
