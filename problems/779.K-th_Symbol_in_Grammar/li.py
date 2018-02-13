# coding=utf-8
# Author: Jianghan LI
# Question: 779.K-th_Symbol_in_Grammar
# Complexity: O(logN)
# Date: 2018-02-09


class Solution(object):

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return bin(K - 1).count('1') & 1
