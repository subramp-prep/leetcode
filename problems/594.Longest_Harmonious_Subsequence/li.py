# coding=utf-8
# Author: Jianghan LI
# Question: 594.Longest_Harmonious_Subsequence
# Date: 2017-05-22 14:50 - 14:56
# Complexity: O(N)


class Solution(object):

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        res = [c[x] + c[x + 1] for x in c if x + 1 in c]
        return max(res) if res else 0

    def findLHS(self, nums):
        c = collections.Counter(nums)
        return max(c[x] + c[x + 1] if c[x + 1] else 0 for x in c) if nums else 0


# 0 wrong try.
