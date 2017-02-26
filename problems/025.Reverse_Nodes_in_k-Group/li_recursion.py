# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-12

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    tail = head
    for _ in range(k):
      if tail:
        tail = tail.next
      else:
        return head
    tail = self.reverseKGroup(tail, k)
    for _ in range(k - 1):
      head.next, head, tail = tail, head.next, head
    head.next = tail
    return head

# OMG 我是天才么 25题一遍AC。。为何contest时候没这个发挥
