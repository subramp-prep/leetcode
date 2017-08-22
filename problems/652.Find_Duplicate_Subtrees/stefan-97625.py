def findDuplicateSubtrees(self, root):
    def tuplify(root):
        if root:
            tuple = root.val, tuplify(root.left), tuplify(root.right)
            trees[tuple].append(root)
            return tuple
    trees = collections.defaultdict(list)
    tuplify(root)
    return [roots[0] for roots in trees.values() if roots[1:]]
