# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-03 09:25-

import random


class Solution(object):

  def majorityElement2(self, nums):
    return [] if nums == [] else [n for n in set([random.choice(nums) for i in range(15)]) if nums.count(n) > len(nums) // 3]

  def majorityElement(self, nums):
    if nums == []:
      return []
    candidate = set([random.choice(nums) for i in range(15)])
    return [n for n in candidate if nums.count(n) > len(nums) // 3]

s = Solution()
print s.majorityElement([])
print s.majorityElement([3, 2, 3])
print s.majorityElement([1, 2, 1, 2, 5])
