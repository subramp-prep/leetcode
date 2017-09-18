# coding=utf-8
# Author: Jianghan LI
# Question: 520.Detect_Capital
# Complexity: O(N)
# Date: 2017-09-09 9:08 - 09:11


class Solution(object):

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return all('A' <= c <= 'Z' for c in word) or all('a' <= c <= 'z' for c in word[1:])

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.upper() or word[1:] == word[1:].lower()


# 字符串有upper和lower函数
