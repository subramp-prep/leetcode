# coding=utf-8
# Author: Jianghan LI
# Question: 1035.Linked_List_Components
# Complexity: O(N)
# Date: 2018-04-12 21:30 - 22:06

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res


############ explanaitons ############

# Take second example in the description:
# liked list:
#     0->1->2->3->4

# I highlighed the subset G in linked list with color red.
# The problem is just to count how many red part there are.
# One red part is one connected components.

# To do this, we just need to count tails of red parts.

# tail = currnt node in setG && (no next node || next node not in setG)
