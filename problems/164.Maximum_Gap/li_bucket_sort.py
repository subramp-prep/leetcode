# coding=utf-8
# Author: Jianghan LI
# Question: 164.Maximum_Gap
# Date: 2017-04-09
# Complexity: O(N)

import math


class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        def sort(a, radix=10):
            """a为整数列表， radix为基数"""
            K = int(math.log(max(a), radix) + 1)  # 用K位数可表示任意整数
            bucket = [[] for i in range(radix)]  # 不能用 [[]]*radix
            for i in range(1, K + 1):  # K次循环
                for val in a:
                    bucket[val % (radix**i) / (radix**(i - 1))].append(val)  # 析取整数第K位数字 （从低到高）
                del a[:]
                for each in bucket:
                    a.extend(each)  # 桶合并
                bucket = [[] for i in range(radix)]
        sort(nums)
        return max(abs(y - x) for x, y in zip(nums, nums[1:]))


############ test case ###########
s = Solution()
print s.maximumGap([1, 3, 100])
