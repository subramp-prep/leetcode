def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)


# improved to 1-linear
def isValidBST(self, root, left=float('-inf'), right=float('inf'),):
    return not root or left < root.val < right and \
        self.isValidBST(root.left, left, root.val) and \
        self.isValidBST(root.right, root.val, right)
