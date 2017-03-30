# coding=utf-8
# Author: Jianghan LI
# Question: 264.Ugly_Number_II
# Date: 2017-03-07 21:41 - 21:45
# Complexity: O(N) O(N)

import math
from itertools import islice


class Solution(object):
	ugly = sorted(2**a * 3**b * 5**c
                      for a in range(32)
                      for b in range(int(1 + 32 * math.log(2, 3)))
                      for c in range(int(1 + 32 * math.log(2, 5))))
    def nthUglyNumber(self, n):

        return next(islice(ugly, n - 1, None))


############ test case ###########
s = Solution()
for i in range(1, 30):
    print i, s.nthUglyNumber(i)
print s.nthUglyNumber(1600)
print 2**32

############ comments ############
