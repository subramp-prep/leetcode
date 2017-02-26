# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-06 13:59-14:10


class Solution(object):

  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    m = Counter()
    maxLen = 0
    for i in set(nums):
      if m[i] > 1:
        continue
      m[i] = m[i + m[i + 1]] = m[i - m[i - 1]] = m[i + 1] + m[i - 1] + 1
      maxLen = max(maxLen, m[i])
    return maxLen

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
print s.longestConsecutive([4, 2, 2, -4, 0, -2, 4, -3, -4, -4, -5, 1, 4, -9, 5, 0, 6, -8, -1, -3, 6, 5, -8, -1, -5, -1, 2, -9, 1])


# 根据soluion_shortest_unordered_map.cpp写的
# 思路是在链子左右两端纪录是链子长度，然后不断更新。
# 遍历每个数时候检查它左右两边的数 然后把这个数，以及它所在链子左右两端，一起赋值为找到链子的长度。
# CPP里max函数可以有赋值语句，所以看起来特别短。
