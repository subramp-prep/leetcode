# coding=utf-8
# Author: Jianghan LI
# Question: Q1
# Complexity: O(N)
# Date: 2017-10-15


class Solution(object):

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cur = s[0]
        count = 1
        L = []
        for i in s[1:]:
            if i == cur:
                count += 1
            else:
                cur = i
                L.append(count)
                count = 1
        L.append(count)
        return sum(min(a, b) for a, b in zip(L, L[1:]))

    def countBinarySubstrings(self, s):
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))


############ test case ###########
s = Solution()
print s.countBinarySubstrings("10101")

############ comments ############
