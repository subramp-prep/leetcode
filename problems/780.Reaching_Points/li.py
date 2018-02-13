# coding=utf-8
# Author: Jianghan LI
# Question: 780.Reaching_Points
# Complexity: O(N)
# Date: 2018-02-11 0:09:55  0:20:10, 2 wrong tries


class Solution(object):

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx <= tx and sy <= ty:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                tx -= max(1, (tx - sx) / ty) * ty
            elif tx < ty:
                ty -= max((ty - sy) / tx, 1) * tx
            else:
                return False
        return False

    def reachingPoints(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and (ty - sy) % sx == 0 or sy == ty and (tx - sx) % sy == 0
############ test case ###########
s = Solution()
print s.reachingPoints(1, 1, 3, 5)  # T
print s.reachingPoints(1, 1, 2, 2)  # F
print s.reachingPoints(1, 1, 1, 1)  # T
print s.reachingPoints(1, 1, 1, 1000000000)  # T
print s.reachingPoints(9, 5, 12, 8)  # F
print s.reachingPoints(1, 5, 2, 8)  # F


############ comments ############
# https://discuss.leetcode.com/topic/120356/easy-and-concise-2-line-solution-python-c-java

# Basic idea:
# If we start from sx,sy, it will be hard to find tx, ty.
# If we start from tx, ty, we can find only one path to go back to sx, sy.

# First line:
# if 2 target points are still bigger than 2 starting point, we reduce target points.
# Second line:
# check if we reduce target points to (x, y+kx) or (x+ky, y)
