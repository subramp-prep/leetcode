# coding=utf-8
# Author: Jianghan LI
# Question: 526.Beautiful_Arrangement
# Date: 2017-05-12 09:00 - 09:24


class Solution(object):
    res = 0

    def countArrangement(self, N):
        def helper(l):
            n = len(l)
            if n == 0:
                self.res += 1
            for i in l:
                if i % n == 0 or n % i == 0:
                    helper(l - {i})
        helper(set(range(1, N + 1)))
        return self.res
