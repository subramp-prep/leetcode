# coding=utf-8
# Author: Jianghan LI
# Question: 565.Array_Nesting
# Date: 2017-05-30 14:28 - 14:32
# Complexity: O(N), 0 wrong try


class Solution(object):

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        res = 0
        for i in nums:
            if i not in seen:
                count = 1
                j = nums[i]
                seen.add(i)
                while j != i:
                    seen.add(j)
                    j = nums[j]
                    count += 1
                res = max(res, count)
        return res

    # better
    def arrayNesting(self, nums):
        seen = set()
        res = 0
        for i in nums:
            count, j = 0, i
            while j not in seen:
                seen.add(j)
                j = nums[j]
                count += 1
            res = max(res, count)
        return res

    # shorter
    def arrayNesting(self, nums):
        seen, res = [0] * len(nums), 0
        for i in nums:
            count, j = 0, i
            while not seen[j]:
                seen[j], count, j = 1, count + 1, nums[j]
            res = max(res, count)
        return res
