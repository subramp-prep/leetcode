class TreeNode(object):

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

from collections import Counter


class Solution(object):

  def findFrequentTreeSum(self, root):
    if not root:
      return []
    c = Counter()

    def getSum(node):
      if not node:
        return 0
      s = node.val + getSum(node.left) + getSum(node.right)
      c[s] += 1
      return s

    getSum(root)
    m = max(c.values())
    return [s for s in c.keys() if c[s] == m]


#### test case #####
s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print s.findFrequentTreeSum(root)
