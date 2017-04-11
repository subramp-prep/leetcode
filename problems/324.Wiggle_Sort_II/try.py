# coding=utf-8
# Author: Jianghan LI
# Question: 324.Wiggle_Sort_II
# Date:
# Complexity: O(N)

import random


class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 1
        for j in range(2, len(nums)):
            print i, j,
            if i & 1:
                if nums[i - 1] < nums[j]:
                    if i < j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 2
                    else:
                        i += 1
                elif nums[i - 1] > nums[j]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    i += 1
            else:
                if nums[i - 1] > nums[j]:
                    if i < j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 2
                    else:
                        i += 1
                elif nums[i - 1] < nums[j]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    i += 1
            print nums
        return i == len(nums)


############ test case ###########
s = Solution()
nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

nums = [2, 1, 1, 2, 2, 3]
nums = [1, 3, 2, 2, 3, 1]

nums = [5, 5, 4, 6]
nums = [1, 2, 9, 5, 5, 5, 5, 5, 8, 2]
s.wiggleSort(nums)
print nums

############ comments ############
# 只能满足没有dup的情况
