# coding=utf-8
# Author: Jianghan LI
# Question: 138.Copy_List_with_Random_Pointer
# Complexity: O(N)
# Date: 2017-08-16 11:53 - 12:11

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        m = {}
        m[head] = RandomListNode(head.label)
        cur = head
        while cur:
            if cur.next:
                m[cur.next] = m[cur].next = RandomListNode(cur.next.label)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]

    # defaultdict是特殊的hashmap，对不存在的key新建一个RandomListNode
    def copyRandomList(self, head):
        d = collections.defaultdict(lambda: RandomListNode(0))
        cur = head
        while cur:
            d[cur].label = cur.label
            if cur.next: d[cur].next = d[cur.next]
            if cur.random: d[cur].random = d[cur.random]
            cur = cur.next
        return d[head] if head else None