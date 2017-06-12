# coding=utf-8
# Author: Jianghan LI
# Question: 605.Can_Place_Flowers
# Date: 2017-06-06 16:41 - 16:52, 0 wrong try
# Complexity: O(N)


class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = zeros = 0
        for i in [0] + flowerbed + [0, 1]:
            if i == 0:
                zeros += 1
            else:
                res += (zeros - 1) / 2 if zeros else 0
                zeros = 0
        return res >= n

    # shorter
    def canPlaceFlowers(self, flowerbed, n):
        res = last = 0
        for i, v in enumerate([1, 0] + flowerbed + [0, 1]):
            if v == 1:
                res += max(0, (i - last - 2) / 2)
                last = i
        return res >= n

    # shorter
    def canPlaceFlowers(self, flowerbed, n):
        return sum((len(i) - 1) / 2 for i in ('0' + ''.join(str(j) for j in flowerbed) + '0').split('1') if i) >= n


############ test case ###########
s = Solution()
print s.canPlaceFlowers([0, 1, 0, 0], 1)

############ comments ############
