# coding=utf-8
# Author: Jianghan LI
# Question: 030.Substring_with_Concatenation_of_All_Words
# Complexity: O(K * len(s) + K * len(words))
# Date: 2017-09-14

import collections


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        k = len(words[0])
        res = []
        for left in range(k):
            d = collections.Counter(words)
            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                d[word] -= 1
                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k
                if left + k * len(words) == right:
                    res.append(left)
        return res


############ test case ###########
s = Solution()
print s.findSubstring("aaa", ["a", "b"])
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])


############ comments ############
