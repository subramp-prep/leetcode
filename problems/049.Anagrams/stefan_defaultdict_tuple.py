# coding=utf-8
import collections


class Solution(object):

  def groupAnagrams(self, strs):
    d = collections.defaultdict(list)
    for s in strs:
      d[tuple(sorted(s))].append(s)
    return map(sorted, d.values())


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


# 对返回值values中的每个value排序了，实际test case并不要求
# 返回d。values即可
