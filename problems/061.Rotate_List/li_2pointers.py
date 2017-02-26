class Solution(object):

  def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None or head.next == None:
      return head
    cur, length = head, 0
    while cur:
      cur = cur.next
      length += 1
    k = k % length
    if k == 0:
      return head
    fast = slow = head
    for _ in range(k):
      fast = fast.next
    while fast.next:
      slow = slow.next
      fast = fast.next
    head, slow.next, fast.next = slow.next, None, head
    return head
