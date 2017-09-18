# coding=utf-8
# Author: Jianghan LI
# Question: 658.Find_K_Closest_Elements
# Complexity: O(K + logN)
# Date: 2017-08-13
# Contest 45, 0:02:35 - 0:20:00, 3 wrong tries

import bisect


class Solution(object):

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = bisect.bisect_left(arr, x)
        if i == 0:
            return arr[:k]
        if i == len(arr):
            return arr[:k]
        if x - arr[i - 1] <= arr[i] - x:
            left = i - 1
            right = i
        else:
            left = i
            right = i + 1
        # print i, left, right
        while right - left < k:
            if left == 0:
                return arr[:k]
            if right == len(arr):
                return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        # print left, right
        return arr[left:right]

    def findClosestElements(self, arr, k, x):
        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            if left == 0:
                return arr[:k]
            if right == len(arr):
                return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]

############ test case ###########
s = Solution()
# print s.findClosestElements([1, 2, 3, 4, 5], 4, 3)
# print s.findClosestElements([1, 2, 3, 4, 5], 4, -1)
# print s.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5)
# print s.findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9)
print s.findClosestElements([1, 2, 3, 3, 6, 6, 7, 7, 9, 9], 8, 8)


############ comments ########:####
# https://discuss.leetcode.com/topic/99203/python-easy-solution-o-k-logn