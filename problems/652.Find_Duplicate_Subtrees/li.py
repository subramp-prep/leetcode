# coding=utf-8
# Author: Jianghan LI
# Question: 652.Find_Duplicate_Subtrees
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def trv(root):
            if not root:
                return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            if struct not in nodes:
                nodes[struct] = root
            elif nodes[struct] != "GET":
                ret.append(nodes[struct])
                nodes[struct] = "GET"
            return struct

        nodes = collections.defaultdict(list)
        ret = []
        trv(root)
        return ret

    def findDuplicateSubtrees(self, root):
        def trv(root):
            if not root:
                return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct

        nodes = collections.defaultdict(list)
        ret = []
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
