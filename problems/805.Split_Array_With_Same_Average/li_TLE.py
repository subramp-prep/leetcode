# coding=utf-8
# Author: Jianghan LI
# Question: 805.Split_Array_With_Same_Average
# Complexity: NP
# Date: 2018-03-24, many wrong tries


class Solution(object):

    def splitArraySameAverage(self, A):
        def find(target, k, i):
            if k == 0:
                return target == 0
            if k + i > len(A):
                return False
            return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
        n, s = len(A), sum(A)
        return any(find(s * i / n, i, 0) for i in range(1, n / 2 + 1) if s * i % n == 0)


############ test case ###########
s = Solution()
print(s.splitArraySameAverage([3863, 703, 1799, 327, 3682, 4330, 3388,
                               6187, 5330, 6572, 938, 6842, 678, 9837, 8256, 6886, 2204, 5262, 6643,
                               829, 745, 8755, 3549, 6627, 1633, 4290, 7]))  # False
print(s.splitArraySameAverage([904, 8738, 6439, 1889, 138, 5771, 8899, 5790, 662,
                               8402, 3074, 1844, 5926, 8720, 7159, 6793, 7402, 9466, 1282, 1748, 434, 842, 22]))  # False
