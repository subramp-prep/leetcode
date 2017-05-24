# coding=utf-8
# Author: Jianghan LI
# Question: 352.Data_Stream_as_Disjoint_Intervals
# Date: 2017-05-21 21:25 - 21:40

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        inf = float('inf')
        self.res = [[-inf, -inf], [inf, inf]]

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        i = bisect.bisect(self.res, [val, val])
        if self.res[i - 1][1] >= val:
            pass
        elif self.res[i - 1][1] + 1 == val:
            if self.res[i][0] == val + 1:
                self.res[i - 1][1] = self.res[i][1]
                self.res[i:] = self.res[i + 1:]
            else:
                self.res[i - 1][1] += 1
        elif self.res[i][0] <= val + 1:
            self.res[i][0] = min(val, self.res[i][0])
        else:
            self.res.insert(i, [val, val])

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.res[1:-1]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

# Brute force， 0 wrong try
