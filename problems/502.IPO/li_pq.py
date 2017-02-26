# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-05


class Solution(object):

  def findMaximizedCapital(self, k, W, Profits, Capital):
    """
    :type k: int
    :type W: int
    :type Profits: List[int]
    :type Capital: List[int]
    :rtype: int
    """
    import Queue
    q = Queue.PriorityQueue()
    projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
    j = 0
    for i in range(k):
      while j < len(projects):
        if projects[j][1] > W:
          break
        else:
          q.put((-projects[j][0], projects[j][0]))
        j = j + 1
      if q.empty():
        break
      else:
        W += q.get()[1]
    return W

s = Solution()
# print s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) # 4
# print s.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) # 0
# print s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) # 6
# print s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) # 4
print s.findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2])  # 5

# Loop k times:
# Add all possible projects (Capital <= W) into the priority queue with the priority = -Profit.
# Get the project with the smallest priority (biggest Profit).
# Add the Profit to W

# https://discuss.leetcode.com/topic/77791/python-solution-by-priority-queue-with-explanation
