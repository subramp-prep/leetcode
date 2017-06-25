# coding=utf-8
# Author: Jianghan LI
# Question: 092.Reverse_Linked_List_II
# Complexity: O(N)
# Date: 2017-06-25 3:16 - 3:38


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        A = dummy
        for _ in range(m - 1):
            A = A.next
        tail = A
        B = cur = A.next
        for _ in range(n - m + 1):
            cur.next, cur, tail = tail, cur.next, cur
        B.next = cur
        A.next = tail
        return dummy.next

# dummy - head - ... - A     - B - ...(cur)  - cur
#     0 - 1    - ... - m - 1 - m - ... - n   - n + 1
