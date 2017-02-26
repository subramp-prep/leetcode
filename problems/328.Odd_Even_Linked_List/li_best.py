# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-09


class Solution(object):

  def oddEvenList(self, head):
    if not head or not head.next:
      return head
    odd = head
    even = evenHead = head.next
    while even and even.next:
      odd.next = odd = odd.next.next
      even.next = even = even.next.next
    odd.next = evenHead
    return head

  def oddEvenList2(self, head):
    if head:
      odd, even, evenHead = head, head.next, head.next
      while even and even.next:
        odd.next, even.next = odd, even = odd.next.next, even.next.next
      odd.next = evenHead
    return head

# 用odd和even维护两个list， 同时even还作为原list的pointer
# while内部为了保持清晰，就没有合并成一行

# oddEvenList2: shortest version
