# coding=utf-8
# Author: Jianghan LI
# Question: Q3
# Complexity: O(N)
# Date: 2018-01-07 0:20:05 - 1:17:34, 1 wrong try

# Definition for an interval.


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        inf = float('inf')
        res = [[-1, inf]]
        for avail in avails:
            i = 0
            for interval in avail:
                start, end = interval
                # start, end = interval.start, interval.end
                while i < len(res):
                    left, right = res[i]
                    if max(left, start) < min(right, end):
                        if left < start < end < right:
                            res[i:i + 1] = [[left, start], [end, right]]
                        elif left < start:
                            res[i:i + 1] = [[left, start]]
                        elif end < right:
                            res[i:i + 1] = [[end, right]]
                        else:
                            res[i:i + 1] = []
                    elif end <= left:
                        break
                    else:
                        i += 1
                # print "go", i, start, end, res
        res2 = []
        for inter in res:
            if inter[0] > 0 and inter[1] < inf:
                res2.append(Interval(*inter))
        return res2


############ test case ###########
s = Solution()
avails = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
print s.employeeFreeTime(avails)  # [[3,4]]

avails = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
print s.employeeFreeTime(avails)  # [[5,6],[7,9]]


avails = [[[7, 24], [29, 33], [45, 57], [66, 69], [94, 99]],
          [[6, 24], [43, 49], [56, 59], [61, 75], [80, 81]],
          [[5, 16], [18, 26], [33, 36], [39, 57], [65, 74]],
          [[9, 16], [27, 35], [40, 55], [68, 71], [78, 81]],
          [[0, 25], [29, 31], [40, 47], [57, 87], [91, 94]]]
print s.employeeFreeTime(avails)  # [[26,27],[36,39],[87,91]]
############ comments ############
