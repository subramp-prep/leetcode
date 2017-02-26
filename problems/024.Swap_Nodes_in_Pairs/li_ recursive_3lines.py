# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 等式左边是第一个节点，第二个节点，第三个节点
    # 等式右边是第二个节点，第一个节点，第三个节点的递归返回
    if head and head.next:
      head, head.next, head.next.next = head.next, head, self.swapPairs(
          head.next.next)
    return head
