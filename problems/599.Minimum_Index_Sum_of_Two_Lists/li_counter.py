# coding=utf-8
# Author: Jianghan LI
# Question: 599.Minimum_Index_Sum_of_Two_Lists
# Date: 2017-05-30, 0 wrong try

from collections import Counter


class Solution(object):

    def findRestaurant(self, l1, l2):
        d = set(l1) & set(l2)
        c = Counter({v: i + 1 for i, v in enumerate(l1) if v in d}) + \
            Counter({v: i + 1 for i, v in enumerate(l2) if v in d})
        res = min(c.values())
        return [i for i, v in c.items() if v == res]


s = Solution()
print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
