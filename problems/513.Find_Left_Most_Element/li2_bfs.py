from collections import deque


class Solution(object):

  def findLeftMostNode(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    bfsList = deque([root])
    while len(bfsList):
      res = None
      for _ in range(len(bfsList)):
        i = bfsList.popleft()
        if res == None:
          res = i.val
        if i and i.left:
          bfsList.append(i.left)
        if i and i.right:
          bfsList.append(i.right)
    return res
