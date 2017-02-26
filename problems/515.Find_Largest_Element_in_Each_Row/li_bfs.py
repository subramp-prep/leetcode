# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None findValueMostElement largestValues

from collections import deque


class Solution(object):

  def findValueMostElement(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return []
    ret = []
    while len(bfsList):
      bfsList2 = []
      ret.append(max([i.val for i in bfsList]))
      for i in bfsList:
        # print i.val
        if i and i.left:
          bfsList2.append(i.left)
        if i and i.right:
          bfsList2.append(i.right)
      bfsList = bfsList2
    return ret

  def findValueMostElement(self, root):
    if not root:
      return []
    bfsList = deque([root])
    ret = []
    while len(bfsList):
      ret.append(max([i.val for i in bfsList]))
      for _ in range(len(bfsList)):
        i = bfsList.popleft()
        if i.left:
          bfsList.append(i.left)
        if i.right:
          bfsList.append(i.right)
    return ret
