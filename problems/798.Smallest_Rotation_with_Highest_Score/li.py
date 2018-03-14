# coding=utf-8
# Author: Jianghan LI
# Question: 798.Smallest_Rotation_with_Highest_Score
# Complexity: O(N)
# Date: 2018-03-10 0:37:33 - 1:14:48, 5 wrong tries

import collections


class Solution(object):

    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        score = 0
        change = [0] * N
        for i in range(N):
            if i - A[i] <= 0:
                score += 1
            change[(i - A[i] + 1) % N] -= 1
            change[(i + 1) % N] += 1
        best_score = score
        K = 0
        for i in range(1, N):
            score += change[i]
            if score > best_score:
                K = i
                best_score = score
        return K

    def bestRotation(self, A):
        N = len(A)
        change = [0] * N
        for i in range(N):
            change[(i - A[i] + 1) % N] -= 1
            change[(i + 1) % N] += 1
        for i in range(1, N):
            change[i] += change[i - 1]
        return change.index(max(change))

    def bestRotation(self, A):
        N = len(A)
        change = [1] * N
        for i in range(N):
            change[(i - A[i] + 1) % N] -= 1
        for i in range(1, N):
            change[i] += change[i - 1]
        return change.index(max(change))

    def bestRotation(self, A):
        N = len(A)
        change = collections.Counter((i - A[i] + 1) % N for i in range(N))
        best = score = res = 0
        for i in range(1, N):
            score -= change[i] - 1
            if best < score:
                best = score
                res = i
        return res

############ test case ###########
s = Solution()
print s.bestRotation([2, 3, 1, 4, 0])  # 3
print s.bestRotation([0, 3, 1, 3, 1])  # 0


############ comments ############
# https://leetcode.com/problems/smallest-rotation-with-highest-score/discuss/118725/easy-and-concise-5-lines-solution-cjavapython/118441?page=1
