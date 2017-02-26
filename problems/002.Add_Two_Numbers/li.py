# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    root = ListNode(0)
    tmp = root
    while l1 or l2 or carry:
      if l1:
        v1 = l1.val
        l1 = l1.next
      else:
        v1 = 0
      if l2:
        v2 = l2.val
        l2 = l2.next
      else:
        v2 = 0
      carry, v = divmod(v1 + v2 + carry, 10)
      tmp.next = ListNode(v)
      tmp = tmp.next
    # root节点是空的，便于循环，实际的root是root.next
    return root.next


############### Note ##################

# python 2.x里面，// 是地板除，/如果有一个数是浮点数就得到小数，如果两个都是整数也是地板除。
# python 3.x里面，// 是地板除，/ 不管两边是不是整数得到的都是小数
# divmod(a,b) 返回 (a//b, a % b)
# 可写成 root = tmp = ListNode(0) 也是对应一个对象
