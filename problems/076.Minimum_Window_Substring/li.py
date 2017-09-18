# coding=utf-8
# Author: Jianghan LI
# Question: 076.Minimum_Window_Substring
# Complexity: O(N)
# Date: 2017-09-06 08:55 - 09:31, 0 wrong try

import collections


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = collections.Counter(t)
        cur = collections.Counter(s)
        if not all(cur[c] >= target[c] for c in target): return ""
        for j, c in enumerate(s[::-1]):
            if c in target:
                if cur[c] == target[c]: break
                cur[c] -= 1
        j = len(s) - j
        for i, c in enumerate(s):
            if c in target:
                if cur[c] == target[c]: break
                cur[c] -= 1
        res = s[i:j]
        while j < len(s):
            # print i,j,s[i:j]
            while j < len(s) and cur[s[i]] == target[s[i]]:
                cur[s[j]] += 1
                j += 1
            # print i,j,s[i:j]
            if cur[s[i]] == target[s[i]]: return res
            while i < len(s) and cur[s[i]] > target[s[i]]:
                cur[s[i]] -= 1
                i += 1
            # print i,j,s[i:j]
            if j - i < len(res): res = s[i:j]
        return res

############ test case ###########
s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")  # BANC
