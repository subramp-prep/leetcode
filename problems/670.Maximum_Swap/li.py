# coding=utf-8
# Author: Jianghan LI
# Question: 670.Maximum_Swap
# Complexity: O(NlogN)
# Date: 2017-09－03
# Contest48 0:10:04 - 0:20:28, 1 wrong try

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        big = sorted(num)[::-1]
        for i in range(len(big)):
            if num[i] != big[i]:
                break
        if i != len(num):
            j = i + (len(num[i:])-num[i:][::-1].index(big[i])-1)
            num[i], num[j] = num[j], num[i]
        return int(''.join(num))

############ test case ###########
s=Solution()
print s.maximumSwap(2736) #7236
print s.maximumSwap(9973) #9973
print s.maximumSwap(1993) #1993

