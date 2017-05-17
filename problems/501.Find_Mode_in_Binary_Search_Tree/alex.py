# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findMode(self, root):
        if not root:
            return []
        count = collections.Counter()

        def dfs(node):
            count[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        max_ct = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_ct]
