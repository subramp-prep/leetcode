# coding=utf-8
# Author: Jianghan LI
# Question: 242.Valid_Anagram
# Date: 2017-04-09 10:50-10:50
# Complexity: O(N+M)


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)
