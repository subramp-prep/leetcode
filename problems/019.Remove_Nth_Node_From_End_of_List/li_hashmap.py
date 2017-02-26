# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-021- 9:33-9:44

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    cur = head
    pos = 0
    count = {}
    while cur:
      count[pos] = cur
      cur = cur.next
      pos += 1
    if pos == n:
      head = head.next
    elif n == 1:
      count[pos - 2].next = None
    else:
      count[pos - n - 1].next = count[pos - n + 1]
    return head

# 用hashmap记录位置索引和node指针。
