class Solution(object):

    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res[::-1]

    def levelOrderBottom2(self, root):
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[-2::-1]
