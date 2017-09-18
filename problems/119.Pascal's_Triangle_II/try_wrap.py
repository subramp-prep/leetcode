import math


class Solution(object):

    def getRow(self, i):
        class Pascal:

            def __getitem__(self, j):
                return math.factorial(i - 1) / math.factorial(i - j - 1) / math.factorial(j)

            def __len__(self):
                return 1
        return Pascal()


############ test case ###########
s = Solution()
p = s.getRow(5)
for i in range(5):
    print p[i]

############ comments ############
