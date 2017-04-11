def levelOrderBottom(self, root):
    queue, res = collections.deque([(root, 0)]), []
    while queue:
        node, level = queue.popleft()
        if node:
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    return res[::-1]
