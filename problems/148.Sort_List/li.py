# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-07 09:30

# Definition for singly - linked list.


class ListNode(object):

  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):

  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    length = 0
    cur = head
    while cur:
      cur = cur.next
      length += 1
    self.sortList(head, length)

  def sortList(self, head, length):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    mid = head.val
    big0 = ListNode()
    small0 = ListNode()
    big = big0
    small = small0
    cur = head.next
    while cur:
      if cur.val > mid:
        big.next = cur
        big = big.next
      else:
        small.next = cur
        small = small.next
      cur = cur.next
    small.next = big0

    cur = small0
    while cur:
      print cur.val
      cur = cur.next
