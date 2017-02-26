# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-17


class Solution:

  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    tmp = ''
    ret = 0
    for i in xrange(0, len(s)):
      tmp = tmp[tmp.find(s[i]) + 1::] + s[i]
      ret = max(len(tmp), ret)
    return ret

########## test case ##########
s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")

# 偷懒用了dp，性能在list.find上有损失。(不知道算不算dp)
# 维护一个str，初始化为空str。
# 然后遍历input中的字符c, str=str.subString[str.indexOf(c)]+1]
# 如果用dict来记录每个字母最近索引，应该可以达到O(n)，见solution.py
# Tags: Hash Table Two Pointers String
