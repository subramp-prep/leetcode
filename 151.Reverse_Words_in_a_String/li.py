# coding=utf-8
# Author: Jianghan LI
# Question: 151.Reverse_Words_in_a_String/li.py
# Date: 24/02/2017 23:15-23:15


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
