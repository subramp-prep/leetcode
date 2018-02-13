# coding=utf-8
# Author: Jianghan LI
# Question: 777.Swap_Adjacent_in_LR_String
# Complexity: O(N)
# Date: 2018-02-09


class Solution(object):

    def canTransform(self, s, e):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s = [(i, v) for i, v in enumerate(s) if v != 'X']
        e = [(i, v) for i, v in enumerate(e) if v != 'X']
        if len(s) != len(e):
            return False
        for (i, a), (j, b) in zip(s, e):
            if a == b == 'R' and i <= j or a == b == 'L' and i >= j:
                continue
            return False
        return True

    def canTransform(self, s, e):
        def canTransform(self, s, e):
        s = [(i, v) for i, v in enumerate(s) if v != 'X']
        e = [(i, v) for i, v in enumerate(e) if v != 'X']
        return len(s) == len(e) and all(a == b == 'R' and i <= j or a ==
                                        b == 'L' and i >= j for (i, a), (j, b) in zip(s, e))
