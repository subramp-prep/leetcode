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
            it = iter(s2)
            return all(i in it for i in s1)

        for s1 in sorted([str for str in c if c[str] == 1], key=len, reverse=True):
            if sum(isSub(s1, s2) for s2 in strs) == 1:
                return len(s1)
        return -1

    def findLUSlength(self, strs):
        return max([len(s1) for s1 in strs
                    if sum(all(c in it for c in s1) for it in map(iter, strs)) == 1]
                   or [-1])


############ test case ###########
s = Solution()
print s.findLUSlength(["aba", "cdc", "eae"])
print s.findLUSlength(["aabbcc", "aabbcc", "cb"])


# https://discuss.leetcode.com/topic/85044/python-simple-explanation
