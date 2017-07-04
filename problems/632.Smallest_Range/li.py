# coding=utf-8
# Author: Jianghan LI
# Question: 632.Smallest_Range
# Date: 2017-07-04
# Complexity: O(NlogK)

import collections
import heapq


class Solution(object):

    # 5.0s
    def smallestRange(self, nums):
        k = len(nums)
        nums = list(heapq.merge(*[[(x, i) for x in num] for i, num in enumerate(nums)]))
        c = collections.Counter()
        i = j = 0
        ret = [nums[-1][0] - nums[0][0], nums[0][0], nums[-1][0]]
        while i < len(nums):
            while j < len(nums) and len(c) < k:
                c[nums[j][1]] += 1
                j += 1
            if len(c) == k:
                ret = min(ret, [nums[j - 1][0] - nums[i][0], nums[i][0], nums[j - 1][0]])
                c[nums[i][1]] -= 1
                # c = collections.Counter()
                if c[nums[i][1]] == 0:
                    del c[nums[i][1]]
            i += 1
        return ret[1:]

    # try faster, 1.0s
    def smallestRange2(self, nums):
        A = collections.defaultdict(set)
        for i, num in enumerate(nums):
            for x in num:
                A[x].add(i)
        c = collections.Counter()
        B = sorted(list(A))
        i = j = 0
        ret = B[0], B[-1]
        while len(c) == len(nums) or j < len(B):
            while j < len(B) and len(c) < len(nums):
                for x in A[B[j]]:
                    c[x] += 1
                j += 1
            while len(c) == len(nums):
                for x in A[B[i]]:
                    c[x] -= 1
                    if c[x] == 0:
                        del c[x]
                i += 1
            if ret[1] - ret[0] > B[j - 1] - B[i - 1]:
                ret = B[i - 1], B[j - 1]
        return ret


############ test case ###########
s = Solution()
A = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]] * 50000
print s.smallestRange([[e for e in a] for a in A])
############ comments ############
# Important: collections.Counter, c1 +- c2 is O(c1 + c2) > O(min(c1, c2))
