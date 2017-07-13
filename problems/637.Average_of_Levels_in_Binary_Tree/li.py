# coding=utf-8
# Author: Jianghan LI
# Question: 637.Average_of_Levels_in_Binary_Tree
# Date: 2017-07-12 16:13 - 16:17, 1 wrong try
# Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        bfs = [root] if root else []
        ret = []
        while bfs:
            ret.append(sum(i.val for i in bfs) / float(len(bfs)))
            bfs = [i for node in bfs for i in (node.left, node.right) if i]
        return ret

############ comments ############
# 1 wrong try: len(bfs) -> float(len(bfs)), fraction division
