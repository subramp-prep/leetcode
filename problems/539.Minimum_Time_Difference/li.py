# coding=utf-8
# Author: Jianghan LI
# Question: 539.Minimum_Time_Difference
# Date: 2017-03-12
# Complexity: O(N)


class Solution(object):

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i, v in enumerate(timePoints):
            timePoints[i] = int(v[:2]) * 60 + int(v[-2:])
        timePoints.sort()
        timePoints.append(timePoints[0] + 1440)
        return min(i[1] - i[0] for i in zip(timePoints, timePoints[1:]))

    def findMinDifference(self, timePoints):
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))


############ test case ###########
s = Solution()
print s.findMinDifference(["23:59", "00:00"])
print s.findMinDifference(["00:06", "13:58", "00:00"])
print s.findMinDifference(["01:01", "02:01"])


# 时间转换成分钟，排序，错位相减，处理首尾的时间差。
# 如果首元素不加1440，也可以模1440来处理。
# t[0]是元素，不能与list相连，t[:1]是切片，可以与list相连
# return min((b - a) % 1440 for a, b in zip(t, t[1:] + t[:1]))
