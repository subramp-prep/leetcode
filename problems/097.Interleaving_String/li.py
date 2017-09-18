# coding=utf-8
# Author: Jianghan LI
# Question: 097.Interleaving_String
# Date: 2017-08-30
class Solution(object):
    seen = set()
    def isInterleave(self, s1, s2, s3):
        if (s1, s2) in self.seen: return False
        self.seen.add((s1, s2))
        if not s1 or not s2: return s1 + s2 == s3
        if s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]): return True
        if s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]): return True
        return False

############ test case ###########
s=Solution()
print s.isInterleave("a","b","ab")

############ comments ############

