def isSymmetric(self, root):
    def isSym(L, R):
        if not L and not R:
            return True
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return False
    return isSym(root, root)


# improved
# return isSym(root, root) 也可以，但是整个树被计算了两遍，性能不太好
def isSymmetric(self, root):
    def isSym(L, R):
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return L == R
    return not root or isSym(root.left, root.right)


# https://leetcode.com/problems/unique-morse-code-words/discuss/120675/easy-and-concise-solution-cjavapython
