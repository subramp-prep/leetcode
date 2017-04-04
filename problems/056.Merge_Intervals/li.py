# coding=utf-8
# Author: Jianghan LI
# Question: 056.Merge_Intervals
# Date: 2017-04-04 10:43 - 10:51
# Complexity: O(NLogN)


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key=lambda i: i.start):
            if len(res) == 0 or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res
