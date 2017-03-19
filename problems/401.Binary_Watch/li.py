# coding=utf-8
# Author: Jianghan LI
# Question: 401.Binary_Watch
# Date: 2017-03-19


class Solution(object):

    def countBit(x):
        ret = 0
        while x:
            ret += x % 2
            x /= 2
        return ret

    dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    for h in range(12):
        for m in range(60):
            n = countBit(h) + countBit(m)
            time = str(m) if m > 9 else '0' + str(m)
            time = str(h) + ':' + time
            dict[n].append(time)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return self.dict.get(num, [])

############ test case ###########
s = Solution()
print s.()

############ comments ############
# Brute force
