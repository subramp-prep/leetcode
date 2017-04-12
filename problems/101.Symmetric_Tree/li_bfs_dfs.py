# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    # dfs
    def isSymmetric(self, root):
        if not root:
            return True
        queue = collections.deque([root.left, root.right])
        while queue:
            left, right = queue.popleft(), queue.pop()
            if left and right and left.val == right.val:
                queue.extend([right.left, right.right])
                queue.extendleft([left.right, left.left])
            elif not left and not right:
                pass
            else:
                return False
        return True

    # bfs
    def isSymmetric(self, root):
        if not root:
            return True
        queue = collections.deque([root.left, root.right])
        while queue:
            left, right = queue.popleft(), queue.popleft()
            if left and right and left.val == right.val:
                queue.extend([left.left, right.right, left.right, right.left])
            elif not left and not right:
                pass
            else:
                return False
        return True
