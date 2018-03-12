# coding=utf-8
# Author: Jianghan LI
# Question: 790.Domino_and_Tromino_Tiling
# Complexity: O(N)
# Date: 2018-02-25 0:11:29 - 0:15:42


class Solution:

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        c = collections.Counter(T)
        s = set(S)
        res = ''
        for i in S:
            res += i * c[i]
        for i in c:
            if i not in s:
                res += i * c[i]
        return res

    def customSortString(self, S, T):
        c, s = collections.Counter(T), set(S)
        return ''.join(i * c[i] for i in S) + ''.join(i * c[i] for i in c if i not in s)

############ test case ###########
s = Solution()
print s.customSortString('cba', 'aabcd')  # cbad

############ comments ############

# https://leetcode.com/problems/custom-sort-string/discuss/116548/2-lines-Python/116715?page=1
