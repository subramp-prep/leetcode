# coding=utf-8
# Author: Jianghan LI
# Question: 125.Valid_Palindrome
# Complexity: O(N)
# Date: 2017-10-20


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]
