# coding=utf-8
# Author: Jianghan LI
# Question: 421.Maximum_XOR_of_Two_Numbers_in_an_Array
# Date:
# Complexity: O(N)


class Solution(object):

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = max(nums)
        bit = 1
        while bit * 2 <= v:
            bit <<= 1
        low = set(i for i in nums if i < bit)
        high = set(i for i in nums if i >= bit)
        res = 0
        if not low:
            return self.findMaximumXOR([i ^ bit for i in nums])
        for i in high:
            for j in low:
                res = max(res, i ^ j)
        return res

############ test case ###########
s = Solution()
nums = [4, 6, 7]
print s.findMaximumXOR(nums)

############ comments ############
