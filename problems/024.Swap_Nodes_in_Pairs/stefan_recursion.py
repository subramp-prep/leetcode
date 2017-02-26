class Solution(object):

  def swapPairs(self, head):
    if head and head.next:
      head.next, head, head.next = \
          self.swapPairs(head.next.next), head.next, head,
    return head

# to save some next
