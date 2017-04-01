# coding=utf-8
# Author: Jianghan LI
# Question: /Users/mac/Work/LeetCode/problems/435.Non-overlapping_Intervals/li_1line.py
# Date: 2017-04-01
# Complexity: O(NlogN)


class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        return len(intervals) - reduce(lambda res, i: (res[0] + 1, i[1]) if i[0] >= res[1] else res,
                                       sorted(intervals, key=lambda i: i[1]), (0, -float('inf')))[0]


############ test case ###########
s = Solution()
print s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])

############ comments ############
