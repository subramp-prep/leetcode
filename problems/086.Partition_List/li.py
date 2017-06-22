# coding=utf-8
# Author: Jianghan LI
# Question: 086.Partition_List
# Date: 2017-06-20 9:13 - 9:25, 1 wrong try.


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = small = ListNode(0)
        h2 = big = ListNode(0)
        while head:
            if head.val < x:
                small.next, small, head = head, head, head.next
            else:
                big.next, big, head = head, head, head.next
        big.next = None
        small.next = h2.next
        return h1.next

# 1 wrong try: big.next = None, 结尾需要闭口。
