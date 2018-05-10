# coding=utf-8
# Author: Jianghan LI
# Question: 813.Largest_Sum_of_Averages
# Complexity: O(KN^2)
# Date: 2018-04-07 0:05:39 - 0:10:06, 0 wrong try


class Solution(object):

    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        memo = {}

        def search(n, k):
            if (n, k) in memo:
                return memo[n, k]
            if n < k:
                return 0
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur, memo[n, k] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)


############ test case ###########
s = Solution()
# print s.largestSumOfAverages([9, 1, 2, 3, 9], 3)
print s.largestSumOfAverages([4, 1, 7, 5, 6, 2], 2)
# print s.largestSumOfAverages([9,1,2,3], 2)
# print s.largestSumOfAverages([10]*100, 100)

############ comments ############
# search(n, k) return the result for n first numbers to k groups.
# It keeps this result to memory. So it's like a DP solution.
