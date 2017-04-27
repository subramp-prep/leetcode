# coding=utf-8
# Author: Jianghan LI
# Question: 516.Longest_Palindromic_Subsequence
# Date: 2017-04-27  8:52 - 9:01
# Complexity: O(N^2)


class Solution(object):

    def longestPalindromeSubseq(self, s):
        res0, res1 = [0] * len(s), [1] * len(s)
        for l in range(2, len(s) + 1):
            res0, res1 = res1, [2 + res0[i + 1] if s[i] == s[i + l - 1]
                                else max(res1[i], res1[i + 1]) for i in range(len(s) - l + 1)]
        return res1[0]
