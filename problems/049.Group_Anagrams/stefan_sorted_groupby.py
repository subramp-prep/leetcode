# coding=utf-8
import itertools


class Solution(object):

  def groupAnagrams(self, strs):
    groups = itertools.groupby(sorted(strs, key=len), sorted)
    return [sorted(members) for _, members in groups]


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# sorted(strs, key=sorted)对strs根据sorted后的字母顺序排序，使得anagrams相邻
# groupby 第二个参数也是key，省略了key=
# sorted和groupby的key要一致，配套使用
# 这里比较巧合的是，key也是sorted函数，看起来比较乱
# groupby返回的是集合迭代器，需要用list转化，也可以用sorted返回排序后的list
