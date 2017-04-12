def isSymmetric(self, root):
    def isSym(L, R):
        if not L and not R:
            return True
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return False
    return isSym(root, root)


# improved
# 整个树被计算了两遍，性能不太好, 最好改成 isSym(root.left, root.right)
def isSymmetric(self, root):
    def isSym(L, R):
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return L == R
    return isSym(root, root)
