# coding=utf-8
# Author: Jianghan LI
# Question: 621.Task_Scheduler
# Date: 2017-06-19
# Complexity: O(M)

import heapq


class Solution(object):

    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        a, b, c, d = float('inf'), float('inf'), float('-inf'), float('-inf')
        for l in arrays:
            a, b, c, d = min(a, l[0]), min(b, max(a, l[0])), max(c, min(d, l[-1])), max(d, l[-1])
        return max(c - a, d - b) if max(l[-1] - l[0] for l in arrays) == d - a else d - a

    def maxDistance(self, arrays):
        a, b = heapq.nsmallest(2, [(l[0], i) for i, l in enumerate(arrays)])
        d, c = heapq.nlargest(2, [(l[-1], i) for i, l in enumerate(arrays)])
        return d[0] - a[0] if d[1] != a[1] else max(d[0] - b[0], c[0] - a[0])


############ test case ###########
s = Solution()
print s.maxDistance([[1, 5], [3, 4]])  # 3
print s.maxDistance([[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]])  # 6
