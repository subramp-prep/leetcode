# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-05 10:30-10:48


class Solution(object):

  def nextGreaterElement(self, findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    import Queue
    q = Queue.PriorityQueue()
    ret = {}
    for i in nums:
      ret[i] = -1
      q.put(i)
      small = q.get()
      while small < i:
        ret[small] = i
        small = q.get()
      q.put(small)
    return [ret[i] for i in findNums]


s = Solution()
print s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
