# coding=utf-8
# Author: Jianghan LI
# Question: 756.Pyramid_Transition_Matrix
# Complexity: O(N)
# Date: 2018-01-02

from collections import defaultdict
from itertools import *


class Solution(object):

    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        f = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed:
            f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1:
                return True
            for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i):
                    return True
            return False

        def pyramid(bottom):
            return len(bottom) == 1 or any(pyramid(i) for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))))
        return pyramid(bottom)


############ test case ###########

bottom = "XYZ"
allowed = ["XYD", "YZE", "DEA", "FFF"]
# True

bottom = "XXYX"
allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# False

s = Solution()
print s.pyramidTransition(bottom, allowed)

############ comments ############
