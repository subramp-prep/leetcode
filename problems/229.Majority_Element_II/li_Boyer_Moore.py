# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-03 08:09-08:22


class Solution(object):

  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    count = {}
    for x in nums:
      if count.has_key(x):
        count[x] += 1
      elif len(count) < 2:
        count[x] = 1
      else:
        for i, j in count.items():
          if j == 1:
            del count[i]
          else:
            count[i] -= 1
    return [n for n in count.keys() if nums.count(n) > len(nums) // 3]


s = Solution()
print s.majorityElement([3, 2, 3])
print s.majorityElement([1, 2, 1, 2, 5])
