# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-18


class Solution(object):

  def threeSum(self, nums):
    res = []
    nums.sort()
    i = 0
    while i < len(nums) - 2:
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      if nums[i] > 0:
        break
      l, r = i + 1, len(nums) - 1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
          l += 1
        elif s > 0:
          r -= 1
        else:
          res.append((nums[i], nums[l], nums[r]))
          # folowing 3 while can avoid the duplications
          while l < r and nums[l] == nums[l + 1]:
            l += 1
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          l += 1
          r -= 1
      while i < len(nums) - 2 and nums[i] == nums[i + 1]:
        i += 1
      i += 1
    return res

########## test case ##########
s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
# Runtime: 175ms, O(n2)
# 遍历＋夹逼，跳过重复解
# python的for循环思想里 i都是从头进入 中间修改不起作用，要想中间起作用，需要使用while
# 在while前面写初始条件，while后写结束条件，while循环尾部写递增值
