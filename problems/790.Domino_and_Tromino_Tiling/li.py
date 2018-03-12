# coding=utf-8
# Author: Jianghan LI
# Question: 791.Custom_Sort_String
# Complexity: O(N)
# Date: 2018-02-25  0:29:45 - 0:53:215, 2 wrong tries


class Solution(object):

    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = [0] * (N + 1)
        B = [1, 1] + [0] * (N - 1)
        for i in range(2, N + 1):
            A[i] = (B[i - 2] + A[i - 1]) % int(1e9 + 7)
            B[i] = (B[i - 1] + B[i - 2] + A[i - 1] * 2) % int(1e9 + 7)
        print A
        print B
        return B[N]

    def numTilings(self, N):
        a, b, c = 0, 1, 1
        for i in range(N - 1):
            a, b, c = b, c, (c + c + a) % int(1e9 + 7)
        return c

############ test case ###########
s = Solution()
print s.numTilings(1)  # 1
print s.numTilings(2)  # 2
print s.numTilings(3)  # 5
print s.numTilings(10)  # 1255
print s.numTilings(30)  # 312342182


############ comments ############
# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116534/Easy-and-Concise-Solution
# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116544/O(N)-time-and-O(1)-space-C++JavaPython
