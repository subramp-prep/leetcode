# coding=utf-8
# Author: Jianghan LI
# Question: 047.Permutations_II
# Date: 2017-03-25
# Complexity: O(N!)


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        ret = []
        seen = set()
        for i, v in enumerate(nums):
            if v not in seen:
                seen.add(v)
                for l in self.permuteUnique(nums[:i] + nums[i + 1:]):
                    ret.append([v] + l)
        return ret

# 轮着拿来放第一个，相同的数字跳过。
# 拆成几行写比较清楚
