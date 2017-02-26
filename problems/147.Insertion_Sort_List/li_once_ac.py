# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-08 11:29-11:35

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def insertionSortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ret = ListNode(0)
    while head:
      toInsert = head
      head = head.next
      cur = ret
      while cur.next and toInsert.val > cur.next.val:
        cur = cur.next
      toInsert.next = cur.next
      cur.next = toInsert
    return ret.next

  def insertionSortList2(self, head):
    ret = ListNode(0)
    while head:
      toInsert, head, cur = head, head.next, ret
      while cur.next and toInsert.val > cur.next.val:
        cur = cur.next
      cur.next, toInsert.next = toInsert, cur.next
    return ret.next

# python 多个赋值可以写成一行
# 并且可以在交换变量数值时候不需要tmp过渡
# ＝右边的值会最先提取，左边的值会在赋值的时候更新
