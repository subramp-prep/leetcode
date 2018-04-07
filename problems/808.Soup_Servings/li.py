# coding=utf-8
# Author: Jianghan LI
# Question: 808.Soup_Servings
# Complexity: O(N)
# Date: 2018-03-31 0:31:49 - 1:22:24, 1 worng try

import math


class Solution(object):
    memo = {}

    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800:
            return 1

        def f(a, b):
            if (a, b) in self.memo:
                return self.memo[a, b]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            res = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
            self.memo[a, b] = res
            return res
        N = math.ceil(N / 25.0)
        res = f(N, N)
        return res

############ test case ###########
s = Solution()
print s.soupServings(50)  # 0.625
print s.soupServings(4800)  # 0.999994994426
print s.soupServings(4801)  # 0.999995382315
print s.soupServings(10000)  # 1

############ comments ############
# wrong try: TLE for big N
# https://leetcode.com/problems/soup-servings/discuss/121711/C++JavaPython-When-N-greater-4800-just-return-1

# servings的操作是必须的，不然会超限
# DP/recursion with memory
# N > 4800
