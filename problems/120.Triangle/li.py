# coding=utf-8
# Author: Jianghan LI
# Question: 120.Triangle
# Date: 2017-06-08 10:09 - 10:17, 0 wrong try
# Complexity: O(N^2) O(1)
# 题目：https://leetcode.com/problems/triangle
# 题解：https://github.com/JianghanLi/LeetCode


class Solution(object):
    # top down

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][i] += triangle[i - 1][i - 1]
        return min(triangle[-1])

    # shorter, 1 linear top down
    def minimumTotal(self, triangle):
        helper = lambda a, b: [min(a[i - 1] if i else float('inf'),
                                   a[i] if i < len(a) else float('inf')) + b[i]
                               for i in range(len(b))]
        return min(reduce(helper, triangle))

    # shorter, 1 linear bottom up
    def minimumTotal(self, triangle):
        return reduce(lambda a, b: [min(a[i], a[i + 1]) + b[i] for i in range(len(b))], reversed(triangle))[0]
