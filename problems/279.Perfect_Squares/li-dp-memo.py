# coding=utf-8
# Author: Jianghan LI
# Question: 279.Perfect_Squares
# Complexity: O(N)
# Date: 2018-00-00 00:00:00 - 00:00:00, 0 wrong try

import sys
sys.setrecursionlimit(10002)

class Solution2(object):

    def __init__(self):
        self.memo = {0: 0}

    def numSquares(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = float('inf')
        i = 1
        while i * i <= n:
            self.memo[n] = min(self.memo[n], self.numSquares(n - i * i) + 1)
            i += 1
        return self.memo[n]


class Solution(object):
    dp = [0]
    def numSquares(self, n):
        for x in range(len(self.dp), n + 1):
            i = 1
            res = float('inf')
            while i * i <= x:
                res = min(res, self.dp[x - i * i] + 1)
                i += 1
            self.dp.append(res)
        return self.dp[n]

############ test case ###########
s = Solution2()
# print s.numSquares(12)  # 3
# print s.numSquares(13)  # 2
# print s.numSquares(8888)  # 2
for i in range(10000, 0, -1):
    s.numSquares(i)  # 2

############ comments ############
# Why time limit??
# 把memo从dict改成list, 可以知道当前最大值,把recursion改成dp
#
