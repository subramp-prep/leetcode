# coding=utf-8
# Author: Jianghan LI
# Question: 168.Excel_Sheet_Column_Title
# Complexity: O(N)
# Date: 2017-09-05


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) / 26
        return res
