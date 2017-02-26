class Solution(object):

  def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None or head.next == None:
      return head
    cur, length = head, 1
    while cur.next:
      cur = cur.next
      length += 1
    k = k % length
    if k = k % length:
      cur.next = head
      for _ in range(length - k):
        cur = cur.next
      head = cur.next
      cur.next = None
    return head

# find tail and reconnect the list
