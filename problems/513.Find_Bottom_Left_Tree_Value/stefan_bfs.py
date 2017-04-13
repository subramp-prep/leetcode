def findBottomLeftValue(self, root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val

# 右中左的遍历
