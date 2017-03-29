# coding=utf-8
# Author: Jianghan LI
# Question: 455.Assign_Cookies
# Date: 29/03/2017 10:03 - 10:09
# Complexity: O(N)


class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i = j = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            i += g[i] <= s[j]
            j += 1
        return i

    def findContentChildren2(self, g, s):
        i, j, g, s = 0, 0, sorted(g), sorted(s)
        while i < len(g) and j < len(s):
            i += g[i] <= s[j]
            j += 1
        return i
