# coding=utf-8
# Author: Jianghan LI
# Question: 060.Permutation_Sequence
# Date: 2017-07-11
# Complexity: O(N^2)

import collections
import math


class Solution(object):

    def getPermutation1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = range(1, n + 1)
        ret = ''
        k -= 1
        for i in l[:]:
            index, k = divmod(k, math.factorial(n - i))
            ret += str(l.pop(index))
        return ret


############ comments ############
# 可以用OrderedDict，index和delet是logN，从而达到O(NlogN)
# 但实际上，并不能优化很多， N=10000左右时，两者用时才接近。
# 很多情况下，O(NlogN)并不会比O(N^2)更好
