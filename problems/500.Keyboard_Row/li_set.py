# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-04 10:09-10:11


class Solution(object):

  def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
      w = set(word.lower())
      if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
        ret.append(word)
    return ret

s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])


# I have used set to check the word.
# I firstly make every line a set of letter.
# Then I check every word if this word set is the subset if any line set.

# https://discuss.leetcode.com/topic/77759/easy-understand-solution-in-7-lines-for-everyone
