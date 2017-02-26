# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-09 9:14 - 9:31

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not (head and head.next):
      return head
    odd = head
    evenHead = cur = even = head.next
    isEven = True
    while cur.next:
      isEven = not isEven
      cur = cur.next
      if isEven:
        even.next = cur
        even = even.next
      else:
        odd.next, odd = cur
        odd = odd.next
    odd.next, even.next = evenHead, None
    return head

# 维护odd和even两个链子 odd.next = evenHead把两个接起来
