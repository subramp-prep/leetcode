# coding=utf-8
# Author: Jianghan LI
# Question: 018.4Sum
# Complexity: O(N)
# Date: 2017-07-16

import collections


class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        sum2 = collections.defaultdict(list)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum2[nums[i] + nums[j]].append((i, j))
        ret = set()
        for i in sum2:
            j = target - i
            if j in sum2 and i <= j:
                for a, b in sum2[i]:
                    for c, d in sum2[j]:
                        if b <= c and len(set([a, b, c, d])) == 4:
                            ret.add((nums[a], nums[b], nums[c], nums[d]))
        return list(ret)


s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
# print s.fourSum([1, 0, -1, 0, -2, 2], 0)
