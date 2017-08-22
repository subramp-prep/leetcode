# coding=utf-8
# Author: Jianghan LI
# Question: 647.Palindromic_Substrings
# Complexity: O(N)
# Date: 2017-08-01 11:44 - 11:51, 0 wrong try


class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def p(i):
            j = k = 0
            while j <= i and j + i < len(s) and s[i - j] == s[i + j]:
                j += 1
            while k <= i and k + i + 1 < len(s) and s[i - k] == s[i + k + 1]:
                k += 1
            return j + k
        return sum(p(i) for i in range(len(s)))
