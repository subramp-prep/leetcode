# coding=utf-8
# Author: Jianghan LI
# Question: 49. Group Anagrams
# Date: 16/02/2017 01:04-01:11


class Solution(object):

  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for i in strs:
      root = ''.join(sorted(list(i)))
      if root in dic:
        dic[root].append(i)
      else:
        dic[root] = [i]
    return dic.values()

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# has_key已经在py3中弃用了，pythonic的方式是in
# 如果是read，可以用get(key,default)或get(key) or default
# root可以不用字符串而用tuple，tuple可以作为字典的key
# sort可以用字典排序，复杂度On
