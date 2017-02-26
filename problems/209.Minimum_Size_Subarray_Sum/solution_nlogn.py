# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-02 11:15


class Solution:

  def minSubArrayLen(self, target, nums):
    result = len(nums) + 1
    for idx, n in enumerate(nums[1:], 1):
      nums[idx] = nums[idx - 1] + n
    left = 0
    for right, n in enumerate(nums):
      if n >= target:
        left = self.find_left(left, right, nums, target, n)
        result = min(result, right - left + 1)
    return result if result <= len(nums) else 0

  def find_left(self, left, right, nums, target, n):
    while left < right:
      mid = (left + right) // 2
      if n - nums[mid] >= target:
        left = mid + 1
      else:
        right = mid
    return left

s = Solution()
# print s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
# print s.minSubArrayLen(4, [1, 4, 4])
print s.minSubArrayLen(11, [1, 2, 3, 4, 5])
