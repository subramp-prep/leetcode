# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-07


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
    if head == None or head.next == None:
      return head
    # step 1. cut the list to two halves
    slow = fast = head
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    prev.next = None
    # step 2. sort each half
    l1 = self.sortList(head)
    l2 = self.sortList(slow)
    # step 3. merge l1 and l2
    return self.merge(l1, l2)

  def merge(self, l1, l2):
    p = l = ListNode(0)
    while l1 != None and l2 != None:
      if l1.val < l2.val:
        p.next = l1
        l1 = l1.next
      else:
        p.next = l2
        l2 = l2.next
      p = p.next
    if l1 != None:
      p.next = l1
    if l2 != None:
      p.next = l2
    return l.next
