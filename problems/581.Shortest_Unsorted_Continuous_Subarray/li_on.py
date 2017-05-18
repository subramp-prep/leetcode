# coding=utf-8
# Author: Jianghan LI
# Question: 581.Shortest_Unsorted_Continuous_Subarray
# Date: 2017-05-17
# Complexity: O(N)


class Solution(object):

    def findUnsortedSubarray(self, nums):
        mi, ma, r, l = float("inf"), -float("inf"), 0, 0
        for i in nums:
            ma = max(ma, i)
            r = r + 1 if i == ma else 0
        for i in nums[::-1]:
            mi = min(mi, i)
            l = l + 1 if i == mi else 0
        return 0 if r == len(nums) else len(nums) - r - l

    def findUnsortedSubarray(self, l):
        reverse = filter(lambda p: p[0] >= p[1], zip(l, l[1::]) if a < b)
        if not reverse:
            return 0
        left, right = min(p[1] for p in reverse), max(p[0] for p in reverse)
        for i in xrange(len(l)):
            if l[i] > left:
                break
        for j in xrange(len(l)):
            if l[-j - 1] < right:
                break
        return len(l) - j - i


# https://discuss.leetcode.com/topic/89661/python-o-n-solution-with-explaination
