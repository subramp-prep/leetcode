# coding=utf-8
import collections


class Solution(object):

  def groupAnagrams(self, strs):
    return reduce(
        lambda d, x: d[tuple(sorted(x))].append(x) or d,
        strs,
        collections.defaultdict(list)).values()

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# 初始值是 collections.defaultdict(list)，默认返回值是list()，也就是[]
# reduce的时候执行d[tuple(sorted(x))].append(x)， 因为不返回d， 所以 or d
# 最后return dict的values
