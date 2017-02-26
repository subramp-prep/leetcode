# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None findLeftMostNode findBottomLeftValue


class Solution(object):

  def findLeftMostNode(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    bfsList = [root]
    while 1:
      bfsList2 = []
      for i in bfsList:
        # print i.val
        if i and i.left:
          bfsList2.append(i.left)
        if i and i.right:
          bfsList2.append(i.right)
      if len(bfsList2):
        bfsList = bfsList2
      else:
        break
    return bfsList[0].val
    # c = {}
    # ret, maxOcc = 0, 0
    # for i in bfsList:
    #   if i:
    #     if not c.get(i.val, 0):
    #       c[i.val] = 1
    #     else:
    #       c[i.val] += 1
    #     if maxOcc < c[i.val]:
    #       ret = i.val
    #       maxOcc = c[i.val]
    # return ret

# For the comments above
# Misunderstood the question but my solution was accepted..
# I took it as to find the first most frequent number
# in the last row of the tree.
# Anyway, contest 19 was really weird for almost every question.

# https://discuss.leetcode.com/topic/79068
