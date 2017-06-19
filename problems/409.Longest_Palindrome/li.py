# coding=utf-8
# Author: Jianghan LI
# Question: 409.Longest_Palindrome
# Date: 2017-06-15 9:18-9:25
# Complexity: O(N)


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min(sum(v & -2 for v in collections.Counter(list(s)).values()) + 1, len(s))

    # using ~1, count even
    def longestPalindrome(self, s):
        return min(sum(v & ~1 for v in collections.Counter(s).values()) + 1, len(s))

    # count odd
    def longestPalindrome(self, s):
        return len(s) - max(sum(v & 1 for v in collections.Counter(s).values()) - 1, 0)
