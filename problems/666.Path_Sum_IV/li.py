# coding=utf-8
# Author: Jianghan LI
# Question: 666.Path_Sum_IV
# Complexity: O(N)
# Date: 2017-08-27
# Contest47, 1:01:00 - 1:18:02, 0 wrong try

class Solution(object):

    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        l = {}
        for i in nums[::-1]:
            a, b, c = i / 100, i / 10 % 10, i % 10
            l[a, b] = max(1, l.get((a + 1, b * 2 - 1), 0) + l.get((a + 1, b * 2), 0))
            s[a, b] = s.get((a + 1, b * 2 - 1), 0) + s.get((a + 1, b * 2), 0) + l[a, b] * c
        return s.get((1, 1), 0)


############ test case ###########
s = Solution()
print s.pathSum([113, 215, 221])  # 12
print s.pathSum([113, 221])  # 4
