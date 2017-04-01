# coding=utf-8
# Author: Jianghan LI
# Question: 435.Non-overlapping_Intervals
# Date: 2017-04-01 10:40 - 10:47
# Complexity: O(N)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        res, last = 0, -float('inf')
        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= last:
                last = i.end
                res += 1
        return len(intervals) - res


# 根据end排序，用last更新前区间的结束的位置
