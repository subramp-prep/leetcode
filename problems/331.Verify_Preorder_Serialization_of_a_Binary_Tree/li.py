# coding=utf-8
# Author: Jianghan LI
# Question: 331.Verify_Preorder_Serialization_of_a_Binary_Tree
# Complexity: O(N)
# Date: 2017-07-22 1:37 - 1:49, 0 wrong try


class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        cur = 0
        l = preorder.split(',')
        for i, c in enumerate(l):
            cur += [1, -1][c == '#']
            if cur < 0 and i + 1 < len(l):
                return False
        return cur == -1

    def isValidSerialization(self, preorder):
        cur = 0
        for c in preorder.split(','):
            if cur < 0:
                return False
            cur += -1 if c == '#' else 1
        return cur == -1
