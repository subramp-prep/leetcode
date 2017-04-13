def findValueMostElement(self, root):
  maxes = []
  row = [root]
  while any(row):
    maxes.append(max(node.val for node in row))
    row = [kid for node in row for kid in (node.left, node.right) if kid]
  return maxes
