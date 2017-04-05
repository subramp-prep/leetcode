# coding=utf-8
# Author: Jianghan LI
# Question: 179.Largest_Number
# Date: 2017-04-05
# Complexity: O(NlogN)


class Solution:
    # @param {integer[]} nums
    # @return {string}

    def largestNumber(self, nums):
        return str(int(''.join(sorted(map(str, nums), lambda x, y: (1, -1)[x + y > y + x]))))

    def largestNumber2(self, nums):
        return ''.join(sorted(map(str, nums), lambda x, y: cmp(y + x, x + y))).lstrip('0') or '0'

############ test case ###########
s = Solution()
print s.largestNumber2([1])
print s.largestNumber2([0, 0])
print s.largestNumber2([2, 23])

############ comments ############
# 比较x+y和y+x的顺序，使用cmp参数，同时可以使用cmp函数比较大小。
# cmp函数，x>y返回1，x==y返回0， x<y返回1.
# 注意返回值需要去除开头的0
# 字符串转int的操作，在别的语言里可能会溢出，应该注意
