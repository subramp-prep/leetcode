def minDepth(self, root):
  if not root:
    return 0
  d = map(self.minDepth, (root.left, root.right))
  return 1 + (min(d) or max(d))

# We need to add the smaller one of the child depths
# except if that's zero, then add the larger one.
