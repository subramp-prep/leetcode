# coding=utf-8
# Author: Jianghan LI
# Question: 401.Binary_Watch
# Date: 2017-03-19


class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["%d:%02d" % divmod(i, 100)
                for i in map(sum, itertools.combinations((1, 2, 4, 8, 16, 32, 100, 200, 400, 800), num))
                if i < 1200 and i % 100 < 60] if num else ["0:00"]

# itertools.combinations
