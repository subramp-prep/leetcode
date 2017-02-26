# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-05 10:48-10:48


class Solution(object):

  def nextGreaterElements(self, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    import Queue
    q = Queue.PriorityQueue()
    ret = [-1] * len(nums)
    for i in range(len(nums)):
      q.put((nums[i], i))
      (small, pos) = q.get()
      while small < nums[i]:
        ret[pos] = nums[i]
        (small, pos) = q.get()
      q.put((small, pos))
    for i in range(len(nums)):
      (small, pos) = q.get()
      while small < nums[i]:
        ret[pos] = nums[i]
        (small, pos) = q.get()
      q.put((small, pos))
    return ret


s = Solution()
print s.nextGreaterElements([1, 2, 1])
