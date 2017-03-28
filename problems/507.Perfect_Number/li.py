# coding=utf-8
# Author: Jianghan LI
# Question: 507.Perfect_Number
# Date: 28/03/2017
# Complexity: O(1)


class Solution(object):
    perfect = set([6, 28, 496, 8128, 33550336, 8589869056])

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in self.perfect
