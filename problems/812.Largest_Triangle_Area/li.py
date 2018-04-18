# coding=utf-8
# Author: Jianghan LI
# Question: 812.Largest_Triangle_Area
# Complexity: O(N^3)
# Date: 2018-04-07 0:00:00 - 0:05:39, 0 wrong try


import itertools


class Solution(object):

    def largestTriangleArea(self, p):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(p)

        def f(p1, p2, p3):
            x1, y1, x2, y2, x3, y3 = p1 + p2 + p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, f(p[i], p[j], p[k]))
        return res

    def largestTriangleArea(self, p):
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
        return max(f(i, j, k) for i, j, k in itertools.combinations(p, 3))

    def largestTriangleArea(self, p):
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
                   for i, j, k in itertools.combinations(p, 3))


############ test case ###########
s = Solution()
print s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
print s.largestTriangleArea([[0, 0] for i in range(50)])


############ comments ############
# f(p1, p2, p3) takes three points and return its area.
# Then we loop on all combinations of three points.
# O(N ^ 3) solution, but N <= 50, so it's fast enough.
