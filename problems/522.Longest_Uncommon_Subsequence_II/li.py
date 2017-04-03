# coding=utf-8
# Author: Jianghan LI
# Question: 522.Longest_Uncommon_Subsequence_II
# Date: 2017-04-03

import collections


class Solution(object):

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = collections.Counter(strs)

        def isSub(s1, s2):
            it = iter(s1)
            return len(s1) >= len(s2) and all(i in it for i in s2)
        for s2 in sorted([str for str in c if c[str] == 1], key=len, reverse=True):
            if sum(map(lambda s1: isSub(s1, s2), strs)) == 1:
                return len(s2)
        return -1


############ test case ###########
s = Solution()
print s.findLUSlength(["aba", "cdc", "eae"])
print s.findLUSlength(["aabbcc", "aabbcc", "cb"])


# https://discuss.leetcode.com/topic/85044/python-simple-explanation
