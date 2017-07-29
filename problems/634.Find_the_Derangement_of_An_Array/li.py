# coding=utf-8
# Author: Jianghan LI
# Question: 634.Find_the_Derangement_of_An_Array
# Date: 2017-07-03 16:56 - 17:12, 2 wrong tries
# Complexity: O(N)


class Solution(object):

    def findDerangement(self, n):
        ret = 0
        mod = 10**9 + 7
        for i in range(2, n + 1):
            ret = (ret * i + (-1 if i & 1 else 1)) % mod
        return ret

    # shorter, not better
    def findDerangement(self, n, mod=10**9 + 7):
        return reduce(lambda x, i: (x * i + (-1) ** i) % mod, range(2, n + 1), 0)

############ test case ###########
s = Solution()
print s.findDerangement(16)

############ comments ############
# Discuss: https://discuss.leetcode.com/topic/94772/python-concise-solution
# wrong try :TLE, %mod for each loop, instead of only at the end
