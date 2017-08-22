# coding=utf-8
# Author: Jianghan LI
# Question: 447.Number_of_Boomerangs
# Complexity: O(N)
# Date: 2017-08-20 2:07 - 2:14

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        n = len(points)
        for i in range(n):
            c = collections.Counter()
            x0, y0 = points[i]
            for j in range(n):
                x1, y1 = points[j]
                dis = (x0 - x1)**2 + (y0 - y1)**2
                c[dis] +=  1
                ret += c[dis]
            for dis in c:
                ret += c[dis]*(c[dis]-1)
        return ret

    def numberOfBoomerangs(self, points):
        ret = 0
        for x0, y0 in points:
            c = collections.Counter()
            for x1, y1 in points:
                d = (x0 - x1)**2 + (y0 - y1)**2
                c[d] +=  1
            for d in c.values(): ret += d * (d-1)
        return ret