# coding=utf-8
# Author: Jianghan LI
# Question: 771.Jewels_and_Stones
# Complexity: O(N)
# Date: 2018-01-28, 0:01:00 - 0:03:15, 0 wrong try


class Solution(object):

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        setJ = set(J)
        return sum(s in setJ for s in S)

############ test case ###########
s = Solution()
J = "aA"
S = "aAAbbbb"
print s.numJewelsInStones(J, S)

############ comments ############
