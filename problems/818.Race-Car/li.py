# coding=utf-8
# Author: Jianghan LI
# Question: 1034.Race_Car
# Complexity: average O(logN)
# Date: 2018-04-14

import heapq
import solution


class Solution(object):

    def __init__(self):
        self.dp = {0: 0}

    def racecar(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if 2**n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2**n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n - 1) + 2**m) + n + m + 1)
        return self.dp[t]


############ test case ###########
s = Solution()
s2 = solution.Solution()

for i in range(100):
    a, b = s.racecar(i), s2.racecar(i)
    if a != b:
        print i, a, b

print s2.racecar(4)
