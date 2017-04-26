# coding=utf-8
# Author: Jianghan LI
# Question: 338.Counting_Bits
# Date: 2017-04-26 8:53 - 8:58


class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) < num + 1:
            res += [i + 1 for i in res]
        return res[:num + 1]

    def countBits(self, num):
        res = [0]
        while len(res) < num + 1:
            res += [i + 1 for i in res[:num + 1 - len(res)]]
        return res[:num + 1]
