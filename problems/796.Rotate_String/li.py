# coding=utf-8
# Author: Jianghan LI
# Question: 796.Rotate_String
# Date: 2018-03-10 0:00:00 - 0:04:53, 0 wrong try


class Solution(object):

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A)):
            if B == A[i:] + A[:i]:
                return True
        return False

    def rotateString(self, A, B):
        return any(B == A[i:] + A[:i] for i in range(len(A)))

    def rotateString(self, A, B):
        return len(A) == len(B) and B in A + A


############ test case ###########
s = Solution()
print s.rotateString(A='abcde', B='cdeab')

############ comments ############
# https://leetcode.com/problems/rotate-string/discuss/118689/1-line-solution-C++JavaPython
