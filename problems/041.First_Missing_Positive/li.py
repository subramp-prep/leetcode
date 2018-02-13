# coding=utf-8
# Author: Jianghan LI
# Question: 041.First_Missing_Positive
# Complexity: O(N)
# Date: 2017-11-18


class Solution(object):

    # O(N), O(N)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        i = 1
        while i in nums:
            i += 1
        return i

    # O(N), O(N), shorter
    def firstMissingPositive(self, nums):
        return min(set(range(1, len(nums) + 2)) - set(collections.Counter(nums)))

    # O(N), O(1)
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        i = 0
        while i < n:
            if i + 1 != nums[i]:
                return i + 1
            i += 1
        return i + 1


############ test case ###########
s = Solution()
print s.firstMissingPositive([3, 4, -1, 1])
print s.firstMissingPositive([])
print s.firstMissingPositive([2, 3, 1])
