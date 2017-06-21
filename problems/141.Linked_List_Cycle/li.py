# coding=utf-8
# Author: Jianghan LI
# Question: 141.Linked_List_Cycle
# Date: 2017-06-19
# Complexity: O(N)


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
        a = b = head
        while b and b.next and a.next != b.next.next:
            a, b = a.next, b.next.next
        return bool(b and b.next)
