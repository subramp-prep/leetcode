# coding=utf-8
# Author: Jianghan LI
# Question: 784.Letter_Case_Permutation
# Date: 2018-02-18 0:06:16

import itertools


class Solution(object):

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = []
        for i in S:
            if '0' <= i <= '9':
                L.append([i])
            else:
                L.append([i.lower(), i.upper()])
        res = []
        for i in itertools.product(*L):
            res.append(''.join(i))
        return res

    def letterCasePermutation(self, S):
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]


############ test case ###########
s = Solution()
print s.letterCasePermutation("a1b2")
print s.letterCasePermutation("12345")

# https://leetcode.com/problems/letter-case-permutation/discuss/115544/Easy-Python-2-line-solution
