# coding=utf-8
# Author: Jianghan LI
# Question: 023.Merge_k_Sorted_Lists
# Date: 2017-05-31 13:39 - 13:50
# Complexity: O(N), 1 wrong try


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        while(any(lists)):
            minV = min(node.val for node in lists if node)
            for i, node in enumerate(lists):
                if node and node.val == minV:
                    lists[i] = node.next
                    cur.next = ListNode(minV)
                    cur = cur.next
        return head.next


# wrong try: for node in lists: node = node.next
# 不会改变lists里的值
