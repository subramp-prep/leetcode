# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-21


class Solution(object):

  def findPermutation(self, s):
    """
    :type s: str
    :rtype: List[int]
    """
    if s == "":
      return [1]
    ret = self.findPermutation(s[1::])
    if s[0] == 'I':
      for i in range(len(ret)):
        ret[i] += 1
      ret.insert(0, 1)
    else:
      for i in range(len(ret)):
        if ret[i] > ret[0]:
          ret[i] += 1
      ret.insert(0, ret[0] + 1)
    return ret

############### test cases ###################
s = Solution()
print s.findPermutation("DI")

# 普通的递归, 但是内存超了，不懂。
# Submission Result: Memory Limit Exceeded
