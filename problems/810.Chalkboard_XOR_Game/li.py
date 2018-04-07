# coding=utf-8
# Author: Jianghan LI
# Question: 810.Chalkboard_XOR_Game
# Complexity: O(N)
# Date: 2018-03-31


class Solution(object):

    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        xor = 0
        for i in nums:
            xor ^= i
        return xor == 0 or len(nums) % 2 == 0


############ comments ############
# https://leetcode.com/problems/chalkboard-xor-game/discuss/121696/C++JavaPython-3-lines-Easy-Solution-with-Complaint-and-Explanation
