# coding=utf-8
# Author: Jianghan LI
# Question: 434.Number_of_Segments_in_a_String/li.py
# Date: 23/02/2017 00:27


class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        for i in range(len(s) - 1):
            res += (s[i] == ' ') ^ (s[i + 1] == ' ')
        return res / 2 + 1 if s else 0

    def countSegments2(self, s):
        res = 0
        for i in range(len(s)):
            res += (i == 0 or s[i - 1] == ' ') and s[i] != ' '
        return res

############ test case ###########
s = Solution()
print s.countSegments("h i")
print s.countSegments("  ")

############ comments ############
