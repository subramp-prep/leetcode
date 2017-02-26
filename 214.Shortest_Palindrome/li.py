# coding=utf-8
# Author: Jianghan LI
# Question: 214.Shortest_Palindrome/li.py
# Date: 26/02/2017


class Solution(object):

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s), 0, -1):
            if s[:i / 2] == s[i - 1:(i - 1) / 2:-1]:
                return s[len(s) - 1:i - 1:-1] + s
        return ""
############ test case ###########
s = Solution()
print s.shortestPalindrome("aacecaaa")

############ comments ############
# 没想到python的暴力还真的能过
# 比较一般，不分类，用字符串长度的奇偶性控制
