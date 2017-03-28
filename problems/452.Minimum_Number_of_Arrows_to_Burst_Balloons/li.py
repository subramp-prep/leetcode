# coding=utf-8
# Author: Jianghan LI
# Question: 452.Minimum_Number_of_Arrows_to_Burst_Balloons
# Date: 28/03/2017
# Complexity: O(NlogN)


class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        last = -float('inf')
        ret = 0
        for start, end in sorted(points, key=lambda x: x[1]):
            if last < start:
                last = end
                ret += 1
        return ret

    def findMinArrowShots2(self, points):
        ret, last_arrow = 0, float('inf')
        for s, e in sorted(points, reverse=True):
            if last_arrow > e:
                last_arrow = s
                ret += 1
        return ret


############ test case ###########
s = Solution()
print s.findMinArrowShots2([[10, 16], [2, 8], [1, 6], [7, 12]])

############ comments ############
# 两个方法一样，一个对start排序自上向下，一个对end排序自下而上。
# https://discuss.leetcode.com/topic/66772/greedy-python-132-ms
