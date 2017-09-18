# coding=utf-8
# Author: Jianghan LI
# Question: 657.Judge_Route_Circle
# Complexity: O(N)
# Date: 2017-08-13
# Contest 45, 0:00:00 - 0:02:35, 0 wrong try


class Solution(object):

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for i in moves:
            if i == "L":
                x -= 1
            if i == "R":
                x += 1
            if i == "D":
                y -= 1
            if i == "U":
                y += 1
        return x == y == 0
