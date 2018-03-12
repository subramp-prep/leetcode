# coding=utf-8
# Author: Jianghan LI
# Question: 760.Find_Anagram_Mappings
# Complexity: O(N)
# Date: 2018-01-07 0:00:00 - 0:07:01, 0 wrong try


class Solution(object):

    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(B):
            if v not in d:
                d[v] = []
            d[v].append(i)
        res = []
        for v in A:
            res.append(d[v].pop())
        return res

    def anagramMappings(self, A, B):
        d = {}
        for i, b in enumerate(B):
            if b not in d:
                d[b] = []
            d[b].append(i)
        return [d[a].pop() for a in A]

    # 1 line, O(N^2)
    def anagramMappings(self, A, B):
        return [B.index(a) for a in A]


############ test case ###########
s = Solution()
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
print s.anagramMappings(A, B)

A = [12, 28, 46, 12, 50]
B = [50, 12, 12, 46, 28]
print s.anagramMappings(A, B)

############ comments ############
