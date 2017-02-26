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
    count = {}
    for i in nums:
      count[i] = True
    maxLen = 0
    for i in count:
      if count[i] == False:
        continue
      left, right = i - 1, i + 1
      while count.get(left):
        count[left] = False
        left = left - 1
      while count.get(right):
        count[right] = False
        right = right + 1
      maxLen = max(maxLen, right - left - 1)
    return maxLen

  def longestConsecutive2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = {}
    for i in nums:
      count[i] = True
    maxLen = 0
    for i in count:
      if count.get(i - 1):
        continue
      right = i + 1
      while count.get(right):
        count[right] = False
        right = right + 1
      maxLen = max(maxLen, right - i)
    return maxLen

s = Solution()
print s.longestConsecutive2([100, 4, 200, 1, 3, 2])


# 用hashmap记录出现数字，一次提升判断每个数出现的效率。
# 遍历hashmap，对于出现的数字，判断左右连续数字最大长度。把遍历的数字都删掉

# 方法2是不修改hashmap，判断是不是起点，然后查找右侧

# 可以学习Stefan，在python中使用set转化。
