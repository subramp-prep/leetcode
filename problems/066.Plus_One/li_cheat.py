# coding=utf-8
# Author: Jianghan LI
# Question: 066.Plus_One
# Complexity: O(N)
# Date: 2017-08-04


class Solution(object):

	def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))

    # another
    def plusOne(self, digits):
        return [int(i) for i in str(reduce(lambda x, y:x * 10 + y, digits) + 1)]
