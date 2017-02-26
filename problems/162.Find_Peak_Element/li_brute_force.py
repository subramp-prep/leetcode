# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-03 10:09-10:11


class Solution(object):

  def findPeakElement2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
      return 0
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        return i
    return len(nums) - 1

  def findPeakElement(self, nums):
    nums.append(float('-inf'))
    return next(i for i in range(len(nums) - 1) if nums[i] > nums[i + 1])

s = Solution()
print s.findPeakElement([1, 2, 3, 4])

# 算法就是简单的暴力算法，
# 最后一行本来想返回i+1的，本以为i==len-1
# 但是产生了 UnboundLocalError: local variable 'i' referenced before assignment
# 后来发现是因为len==2时候不会进入1==len-1，不会进入循环，i不会被赋值

# 后来使用了python的查找下一个的函数next
# 在数组尾部加入负无穷，也可以避免边界的查找
# I add -infinity to the end of nums in order to avoid all boundary checks.
# Then I simply find the first element which is bigger than its next one.
# https://discuss.leetcode.com/topic/77703/two-lines-force-brute-search
