# coding=utf-8
# Author: Jianghan LI
# Question: 686.Repeated_String_Match
# Complexity: O(N)
# Date: 2017-10-23


class Solution(object):

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = (A * (len(B) / len(A) + 2)).find(B)
        if i < 0:
            return -1
        return -((i + len(B)) / -len(A))
