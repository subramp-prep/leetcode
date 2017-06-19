# coding=utf-8
# Author: Jianghan LI
# Question: 041.First_Missing_Positive
# Date: 2017-06-11 2:26 - 2:31, 1 wrong try
# Complexity: O(NlogN), O(N)


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = sorted(i for i in set(nums) if i > 0)
        for i, v in enumerate(pos):
            if i + 1 != v:
                return i + 1
        return len(pos) + 1

    # shorter
    def firstMissingPositive(self, nums):
        return min(set(range(1, len(nums) + 2)) - set(collections.Counter(nums)))

# Wrong try: be care of duplicate numbers.
