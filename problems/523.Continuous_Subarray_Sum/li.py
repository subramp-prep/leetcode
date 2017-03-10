# coding=utf-8
# Author: Jianghan LI
# Question: 523.Continuous_Subarray_Sum
# Date: 10/03/2017
# Complexity: O(N) O(N)


class Solution(object):

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        r = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            r = (r + num) % k if k else r + num
            if r not in seen:
                seen[r] = i
            if i - seen[r] > 1:
                return True
        return False


############ comments ############
# To deal with the case k=0, in my version, i don't calculate the remainder divided by k.


# https://discuss.leetcode.com/topic/80841/python-with-explanation-62ms-time-o-min-n-k-mostly/9
