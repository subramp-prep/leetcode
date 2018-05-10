import scipy.sparse
import numpy as np


class Solution(object):

    def findCircleNum(self, M):
        M = np.matrix(M, dtype='bool')
        return scipy.sparse.csgraph.connected_components(M)[0]

# https://discuss.leetcode.com/topic/85108/oneliner-p
# SciPy is an open source Python library used for scientific computing and technical computing. NumPy and SciPy are the most common lib Data Analysts use. And they made Python very popular.
# Yeah, it's not part of Python. Might've gotten installed here when
# LeetCode added problems involving randomization, to use it in the judge
# for checking the randomness of solutions. At least I think that's where
# I noticed it first.

############ test case ###########
s = Solution()
print s.findCircleNum([[1, 1, 0],
                       [1, 1, 0],
                       [0, 0, 1]])
