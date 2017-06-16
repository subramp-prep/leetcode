# coding=utf-8
# Author: Jianghan LI
# Question: 611.Valid_Triangle_Number
# Date: 2017-06-12 11:48 - 11:57, 1 wrong try
# Complexity: O(N^2)


class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        res = 0
        nums.sort()
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res

# 1 wrong try: O(N^3) brute force timeout
