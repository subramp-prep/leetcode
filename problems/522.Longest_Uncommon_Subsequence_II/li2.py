# coding=utf-8
# Author: Jianghan LI
# Question: 522.Longest_Uncommon_Subsequence_II
# Complexity: O(N)
# Date: 2017-08-03

# 5:22

import collections


class Solution(object):

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = collections.Counter(strs)
        unique = list(i for i in c if c[i] == 1)
        duplicate = list(i for i in c if c[i] > 1)
        sorted_unique = sorted(unique, key=lambda i: -len(i))

        def isNotSub(a, b):
            it = iter(b)
            return not all(i in it for i in a)

        for i in sorted_unique:
            if all(isNotSub(i, j) for j in duplicate):
                return len(i)
            else:
                duplicate.append(i)
        return -1

############ test case ###########
s = Solution()
print s.findLUSlength(["aba", "cdc", "eae"])
print s.findLUSlength(["aabbcc", "aabbcc", "cb"])
