def reverseKGroup(self, head, k):
  dummy = jump = ListNode(0)
  dummy.next = l = r = head

  while True:
    count = 0
    while r and count < k:   # use r to locate the range
      r = r.next
      count += 1
    if count == k:  # if size k satisfied, reverse the inner linked list
      pre, cur = r, l
      for _ in range(k):
        cur.next, cur, pre = pre, cur.next, cur  # standard reversing
      jump.next, jump, l = pre, l, r  # connect two k-groups
    else:
      return dummy.next
