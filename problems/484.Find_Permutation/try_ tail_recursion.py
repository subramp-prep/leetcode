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
    return self.recursive(s, [1])

  def recursive(self, s, ret):
    if s == "":
      return ret
    if s[-1] == 'I':
      for i in range(len(ret)):
        ret[i] += 1
      ret.insert(0, 1)
    else:
      for i in range(len(ret)):
        if ret[i] > ret[0]:
          ret[i] += 1
      ret.insert(0, ret[0] + 1)
    return self.recursive(s[0:len(s) - 1], ret)

    ############### test cases ###################
s = Solution()
print s.findPermutation("I")

# 改用了尾递归，但是时间笑了
# Submission Result: Time Limit Exceeded
