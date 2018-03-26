# coding=utf-8
# Author: Jianghan LI
# Question: 806.Number_of_Lines_To_Write_String
# Complexity: O(N)
# Date: 2018-03-24 0:00:00 - 0:07:08, 0 wrong try


class Solution(object):

    def numberOfcurs(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        cur = 0
        res = 1
        for i in S:
            i = ord(i) - ord('a')
            width = widths[i]
            if width + cur > 100:
                cur = width
                res += 1
            else:
                cur += width
        return [res, cur]

    def numberOfcurs(self, widths, S):
        res, cur = 1, 0
        for i in S:
            width = widths[ord(i) - ord('a')]
            res += 1 if cur + width > 100 else 0
            cur = width if cur + width > 100 else cur + width
        return [res, cur]


############ test case ###########
s = Solution()

widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "bbbcccdddaaa"
print s.numberOfcurs(widths, S)

widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "abcdefghijklmnopqrstuvwxyz"
print s.numberOfcurs(widths, S)
