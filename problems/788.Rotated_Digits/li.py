# coding=utf-8
# Author: Jianghan LI
# Question: 788.Rotated_Digits
# Complexity: O(N)
# Date: 2018-02-25  0:00:00 - 0:11:29, 1 wrong try


class Solution:

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s1, s2 = set([1, 8, 0]), set([1, 8, 0, 6, 9, 2, 5])

        def isGood(x):
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))

    def rotatedDigits(self, N):
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = map(int, str(N))
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7**(len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))

    # shorter, less efficient
    def rotatedDigits2(self, N):
        s1, s2 = set([0, 1, 8]), set([0, 1, 8, 2, 5, 6, 9])
        res = 0
        N = map(int, str(N))
        for i, v in enumerate(N):
            for j in range(v):
                cur = set(N[:i]) | {j}
                if cur.issubset(s2):
                    res += 7**(len(N) - i - 1)
                if cur.issubset(s1):
                    res -= 3**(len(N) - i - 1)
        return res + (set(N).issubset(s2) and not set(N).issubset(s1))


############ test case ###########
s = Solution()
print s.rotatedDigits(1)  # 0
print s.rotatedDigits(2)  # 1
print s.rotatedDigits(3)  # 1
print s.rotatedDigits(5)  # 2
print s.rotatedDigits(6)  # 3
print s.rotatedDigits(8)  # 3
print s.rotatedDigits(9)  # 4
print s.rotatedDigits(2537)  # 800
print s.rotatedDigits(10000)  # 2230
############ comments ############
# 1,8,0
# 6,9,2,5


# https://leetcode.com/problems/escape-the-ghosts/discuss/116522/Easy-and-Concise-SolutionC++JavaPython
