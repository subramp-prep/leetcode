# coding=utf-8
# Author: Jianghan LI
# Question: 438.Find_All_Anagrams_in_a_String
# Complexity: O(N)
# Date: 2017-09-12 8:47 - 09:02, 0 wrong try

import collections


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        need = len(p)
        i = j = 0
        c = collections.Counter(p)
        while j < len(s):
            if c[s[j]] > 0:
                need -= 1
            if s[j] in c:
                c[s[j]] -= 1
            j += 1
            # print s[i:j], need, c
            if j - i == len(p):
                if need == 0:
                    res.append(i)
                if s[i] in c:
                    c[s[i]] += 1
                if c[s[i]] > 0:
                    need += 1
                i += 1
        return res

    def findAnagrams(self, s, p):
        res = []
        need = i = j = 0
        c = collections.Counter(p)
        while j < len(s):
            need += c[s[j]] > 0
            c[s[j]] -= 1
            j += 1
            # print s[i:j], need, c
            if need == len(p): res.append(i)
            if j - i == len(p):
                c[s[i]] += 1
                need -= c[s[i]] > 0
                i += 1
        return res

############ test case ###########
s = Solution()
print s.findAnagrams("cbaebabacd", "abc")
