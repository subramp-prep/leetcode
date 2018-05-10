# coding=utf-8
# Author: Jianghan LI
# Question: 809.Expressive_Words
# Complexity: O(N)
# Date: 2018-03-31 0:09:36 - 0:31:49, 0 wrong try


class Solution(object):

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S:
            return 0

        def test(word):
            N = len(word)
            i = 0
            L = []
            for j in range(1, N):
                if word[i] == word[j]:
                    continue
                L.append((word[i], j - i))
                i = j
            L.append((word[j], N - i))
            return L

        def extend(C1, C2):
            if len(C1) != len(C2):
                return False
            for (c1, n1), (c2, n2) in zip(C1, C2):
                if c1 != c2:
                    return False
                if n1 == n2:
                    continue
                if n1 >= 3:
                    continue
                return False
            return True

        S2 = test(S)
        res = 0
        for word in words:
            if extend(S2, test(word)):
                res += 1
        return res

    def expressiveWords(self, S, words):
        def check(S, W):
            i, j, n, m = 0, 0, len(S), len(W)
            while i < n and j < m:
                while i < n and j < m and S[i] == W[j]:
                    i, j = i + 1, j + 1
                if i == n and j == m:
                    return True
                while i > 0 and i < n and S[i] == S[i - 1]:
                    i += 1
                if i < 3 or S[i - 1] != S[i - 2] or S[i - 2] != S[i - 3]:
                    return False
            return i == n and j == m
        return sum(check(S, W) for W in words)

############ test case ###########
s = Solution()
print s.expressiveWords(S="heeellooo", words=["hello", "hi", "helo"])
print s.expressiveWords(S="hee", words=["he"])
print s.expressiveWords(S="aaa", words=["aaaa"])


############ comments ############
# https://leetcode.com/problems/expressive-words/discuss/122660/C++JavaPython-solution
