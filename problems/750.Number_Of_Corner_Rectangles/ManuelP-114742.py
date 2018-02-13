from collections import Counter
from itertools import *


class Solution(object):

    def countCornerRectangles(self, grid):
        d = Counter(chain(*(combinations(compress(count(), row), 2) for row in grid)))
        return sum(x * (x - 1) / 2 for x in d.values())

############ test case ###########
s = Solution()
print s.countCornerRectangles([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])  # 9
print s.countCornerRectangles([[1, 0, 0, 1, 0],
                               [0, 0, 1, 0, 1],
                               [0, 0, 0, 1, 0],
                               [1, 0, 1, 0, 1]])  # 1
print s.countCornerRectangles([[1, 1, 1, 1]])  # 0
