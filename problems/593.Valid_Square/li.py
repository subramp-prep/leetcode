# coding=utf-8
# Author: Jianghan LI
# Question: 593.Valid_Square
# Date: 2017-05-22


class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])

        def isRight(a, b, c):
            return (a[1] - b[1]) * (c[1] - b[1]) + (a[0] - b[0]) * (c[0] - b[0]) == 0 and abs(a[1] - b[1]) == abs(c[0] - b[0]) and a != b
        return isRight(p2, p1, p3) and isRight(p2, p4, p3)
