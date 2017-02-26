# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-30


class Solution(object):

  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
      if nums[i] > 0:
        # print "i =", i, nums
        tmp = nums[i]
        nums[i] = 0
        while nums[tmp - 1] > 0:
          # print "tmp =", tmp, nums
          tmp2 = nums[tmp - 1]
          nums[tmp - 1] = -1
          tmp = tmp2
        nums[tmp - 1] -= 1
    return filter(lambda i: nums[i - 1] == -2, range(1, len(nums) + 1))


s = Solution()
print s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
print s.findDuplicates([2, 2])


# 对于原题的例子：[4, 3, 2, 7, 8, 2, 3, 1]
# i = 0 [4, 3, 2, 7, 8, 2, 3, 1]
# tmp = 4 [0, 3, 2, 7, 8, 2, 3, 1]
# tmp = 7 [0, 3, 2, -1, 8, 2, 3, 1]
# tmp = 3 [0, 3, 2, -1, 8, 2, -1, 1]
# tmp = 2 [0, 3, -1, -1, 8, 2, -1, 1]
# i = 4 [0, -1, -2, -1, 8, 2, -1, 1]
# tmp = 8 [0, -1, -2, -1, 0, 2, -1, 1]
# i = 5 [-1, -1, -2, -1, 0, 2, -1, -1]
# 思想就是，用tmp用来记录目前取出来的数，把这个数作为index，在数组对应位置，用0,-1, -2来记录这个数出现次数
# 对应位置原来的数就再取出放在tmp里
