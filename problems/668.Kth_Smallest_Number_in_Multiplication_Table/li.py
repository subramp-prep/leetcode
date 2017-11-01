# coding=utf-8
# Author: Jianghan LI
# Question: 668.Kth_Smallest_Number_in_Multiplication_Table
# Complexity: O(MlogMN)
# Date: 2017-08-27

from heapq import *


class Solution(object):

    def findKthNumber(self, m, n, k):
        low, high = 1, m * n
        while low < high:
            mid = (high + low) / 2
            c = sum(min(mid / i , n) for i in range(1, m + 1))
            if c >= k: high = mid
            else: low = mid + 1
        return low

############ test case ###########
s = Solution()
print s.findKthNumber(3, 4, 12)

############ comments ############
# 二分法
