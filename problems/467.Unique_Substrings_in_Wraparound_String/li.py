# coding=utf-8
# Author: Jianghan LI
# Question: 467.Unique_Substrings_in_Wraparound_String
# Complexity: O(N)
# Date: 2017-10-07


class Solution(object):

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pre = l = 0
        res = [0] * 26
        p = [ord(i) - ord('a') for i in p]
        for i in p:
            l = l + 1 if (pre + 1) % 26 == i else 1
            pre = i
            res[i] = max(res[i], l)
        return sum(res)

    def findSubstringInWraproundString2(self, p):
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())


############ test case ###########
s = Solution()
p = "abbc"


print s.findSubstringInWraproundString(p)
print s.findSubstringInWraproundString2(p)
############ comments ############
