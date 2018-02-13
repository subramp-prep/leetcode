# coding=utf-8
# Author: Jianghan LI
# Question: 775.Global_and_Local_Inversions
# Complexity: O(N)
# Date: 2018-01-28  0:03:15 - 0:17:43, 2 wrong tries


class Solution(object):

    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True

    def isIdealPermutation(self, A):
        cmax = 0
        for a, b in zip(A, A[2:]):
            cmax = max(cmax, a)
            if cmax > b:
                return False
        return True

    def isIdealPermutation(self, A):
        return all(abs(i - v) <= 1 for i, v in enumerate(A))


############ test case ###########
s = Solution()
print s.isIdealPermutation([1, 0, 2])  # T
print s.isIdealPermutation([1, 2, 0])  # F
print s.isIdealPermutation([0])  # T
print s.isIdealPermutation([2, 0, 3, 1])  # False


############ comments ############
