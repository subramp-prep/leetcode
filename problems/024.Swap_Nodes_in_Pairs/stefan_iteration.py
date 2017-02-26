def swapPairs(self, head):
  pre, pre.next = self, head
  while pre.next and pre.next.next:
    a = pre.next
    b = a.next
    pre.next, b.next, a.next = b, a, b.next
    pre = a
  return self.next


def swapPairs(self, head):
  pre, pre.next = self, head
  while pre.next and pre.next.next:
    pre.next, pre.next.next, pre.next.next.next = \
        pre.next.next, pre.next, pre.next.next.next
    pre = pre.next.next
  return self.next


# Why use self?
# Because I can.
# I could create the usual dummy ListNode object instead,
# but apparently I didn't feel like it.
# Maybe I was lazy, maybe I wanted to show that it's possible.

# Yeah, I had considered to merge the two lines,
# but I found it long enough already :-).
# And it would be mixing two really separate issues,
# doing the swap and moving forward.
