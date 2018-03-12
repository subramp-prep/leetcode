# coding=utf-8
# Author: Jianghan LI
# Question: 786.K-th_Smallest_Prime_Fraction/li.py

import bisect


class Solution(object):

    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        l = 0
        r = 1
        cur = 0
        N = len(A)
        while cur != K:
            m = (l + r) / 2
            cur = 0
            res = (0, 1)
            for i in range(N):
                j = bisect.bisect(A, A[i] / m)
                if j < N and res[1] * A[i] - res[0] * A[j] > 0:
                    res = (A[i], A[j])
                cur += N - j
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                break
        return res

    def kthSmallestPrimeFraction(self, A, K):
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])


############ test case ###########
s = Solution()
print(s.kthSmallestPrimeFraction(A=[1, 2, 3, 5], K=3))  # (2, 5)
print(s.kthSmallestPrimeFraction([1, 3, 5, 29, 53, 79, 83, 97], 24))  # (53, 83)


############ comments ############
# https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115538/Python-solution-using-Binary-Search
