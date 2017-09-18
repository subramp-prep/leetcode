# coding=utf-8
# Author: Jianghan LI
# Question: 659.Split_Array_into_Consecutive_Subsequences
# Complexity: O(N)
# Date: 2017-08-13 0:34:22 - 1:04:47, 3 wrong try

import collections


class Solution(object):

    def isPossible(self, nums):
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True


############ test case ###########
s = Solution()
# print s.isPossible([1, 2, 3, 3, 4, 5])  # T
# print s.isPossible([1, 2, 3, 3, 4, 4, 5, 5])  # T
print s.isPossible([1, 2, 3, 4, 4, 5])  # F
# print s.isPossible([1, 2, 3, 4, 6, 7, 8, 9, 10, 11])  # F
# print s.isPossible([4, 5, 6, 7, 7, 8, 8, 9, 10, 11])  # T

############ comments ############
# https://discuss.leetcode.com/topic/99542/python-esay-understand-solution
# I used a greedy alorithme.
# leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
# endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
# Then I tried to split the nums one by one.
# If I could neigther add a number to the end of a existing consecutive
# subsequence nor find two following number in the left, I returned False
