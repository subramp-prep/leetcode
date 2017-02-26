# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-03 13:07


class Solution(object):

  def findPeakElement(self, nums):
    if len(nums) == 1:
      return 0
    mid = len(nums) // 2
    if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
      return mid
    return mid + self.findPeakElement(nums[mid:]) if nums[mid] > nums[mid - 1] else self.findPeakElement(nums[:mid])

s = Solution()
print s.findPeakElement([1])
print s.findPeakElement([3, 2])
print s.findPeakElement([2, 3])
print s.findPeakElement([1, 2, 3, 4, 1])
