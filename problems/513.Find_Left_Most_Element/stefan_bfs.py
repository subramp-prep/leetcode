def findLeftMostNode(self, root):
  queue = [root]
  for node in queue:
    queue += filter(None, (node.right, node.left))
  return node.val
