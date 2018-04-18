# coding=utf-8
# Author: Jianghan LI
# Question: 1034.Race_Car
# Complexity: O(NlogN)
# Date: 2018-04-14


import heapq
import solution


class Solution(object):

    def racecar(self, target):
        dp = [0] + [float('inf')] * target
        for i in range(1, target + 1):
            n = i.bit_length()
            if 2**n - 1 == i:
                dp[i] = n
                continue
            dp[i] = dp[2**n - 1 - i] + n + 1
            for m in range(n - 1):
                dp[i] = min(dp[i], dp[i - 2**(n - 1) + 2**m] + n + m + 1)
        return dp[target]

############ test case ###########
s2 = solution.Solution()
s = Solution()

for i in range(100):
    a, b = s.racecar(i), s2.racecar(i)
    print a
    if a != b:
        print i, a, b


############ comments ############
# n is the length i in binary, so we have 2 ^ (n - 1) <= i < 2 ^ n - 1

# After n instructions of 'A', we go ahead for 1 + 2 + ... + 2 ^ (n - 1) = 2 ^ n - 1

# One possible option is that we take N instruction of 'A' and one 'R', hoping we move closer to our target.

# The other option is that we take N - 1 instruction of 'A' and one 'R'.

# Then we take up to n - 1 instructions of 'A'. In this way, I get further but it's still better than start point.
