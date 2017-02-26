# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-02 11:15


class Solution(object):

  def minSubArrayLen(self, s, nums):
    ret = len(nums) + 1
    left = right = tmpSum = 0
    while right < len(nums):
      tmpSum += nums[right]
      right += 1
      while tmpSum >= s:
        ret = min(ret, right - left)
        tmpSum -= nums[left]
        left += 1
    return ret if ret <= len(nums) else 0

s = Solution()
# print s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
# print s.minSubArrayLen(4, [1, 4, 4])
print s.minSubArrayLen(11, [1, 2, 3, 4, 5])
