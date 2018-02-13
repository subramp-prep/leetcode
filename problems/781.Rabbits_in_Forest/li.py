# coding=utf-8
# Author: Jianghan LI
# Question: 781.Rabbits_in_Forest
# Complexity: O(N)
# Date: 2018-02-11 0:09:06 - 0:09:55, 0 wrong try

import collections
import math


class Solution(object):

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        c = collections.Counter(answers)
        res = 0
        for i in c:
            res += math.ceil(float(c[i]) / (i + 1)) * (i + 1)
        return int(res)

    def numRabbits(self, answers):
        c = collections.Counter(answers)
        res = 0
        for i in c:
            res += (c[i] + i) / (i + 1) * (i + 1)
        return res

    def numRabbits(self, answers):
        c = collections.Counter(answers)
        return sum((c[i] + i) / (i + 1) * (i + 1) for i in c)


############ test case ###########
s = Solution()
print s.numRabbits([1, 1, 2])


############ comments ############
# https://discuss.leetcode.com/topic/120341

# If x+1 rabbits have same color, then we get x+1 rabbits who all answer x.
# now n rabbits answer x.
# If n%(x+1)==0, we need n/(x+1) groups of x+1 rabbits.
# If n%(x+1)!=0, we need n/(x+1) + 1 groups of x+1 rabbits.

# the number of groups is math.ceil(n/(x+1)) and it equals to (n+i)/(i+1) , which is more elegant.
