# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-18


class Solution(object):

  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
      return ""
    strs.sort()

    for i in xrange(min(len(strs[0]), len(strs[-1]))):
      if strs[0][i] != strs[-1][i]:
        i = i - 1
        break
    return strs[0][0:i + 1]

########## test case ##########
s = Solution()
print s.longestCommonPrefix(["a", "b"])

# Runtime: 65 ms, O(nlogn)
# Sort the array first, and then you can simply compare the first and last
# elements in the sorted array.
