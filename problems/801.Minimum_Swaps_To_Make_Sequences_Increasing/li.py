# coding=utf-8
# Author: Jianghan LI
# Question: 801.Minimum_Swaps_To_Make_Sequences_Increasing
# Complexity: O(N)
# Date: 2018-03-17 0:16:43 - 0:29:45, 1 wrong try


class Solution(object):

    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                not_swap[i] = not_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                not_swap[i] = min(not_swap[i], swap[i - 1])
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
        return min(swap[-1], not_swap[-1])

############ test case ###########
s = Solution()
print s.minSwap(A=[1, 3, 5, 4], B=[1, 2, 3, 7])
print s.minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9])
