# coding=utf-8
# Author: Jianghan LI
# Question: 767.Reorganize_String
# Complexity: O(NK)
# Date: 2018-01-21  0:00:08 － 0:10:16, 0 wrong try


import collections
import itertools


class Solution(object):

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = collections.Counter(S)
        if max(c.values()) <= (len(S) + 1) / 2:
            res = ""
            while c:
                out = c.most_common(2)
                if len(out):
                    res += out[0][0]
                    c[out[0][0]] -= 1
                if len(out) > 1:
                    res += out[1][0]
                    c[out[1][0]] -= 1
                c += collections.Counter()
            return res
        return ""

############ test case ###########
s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
print(s.reorganizeString("aabcc"))
print(s.reorganizeString("abccba"))


for i in range(26):
    for j in range(26):
        a = chr(97 + i)
        b = chr(97 + j)
        res = s.reorganizeString(a * 5 + b * 5)
        if res and res not in [(a + b) * 5, (b + a) * 5]:
            print(res)


for i in range(26):
    for j in range(26):
        a = chr(97 + i)
        b = chr(97 + j)
        res = s.reorganizeString(a * 2 + b * 2)
        if res and res not in [(a + b) * 2, (b + a) * 2]:
            print(res)

############ comments ############
