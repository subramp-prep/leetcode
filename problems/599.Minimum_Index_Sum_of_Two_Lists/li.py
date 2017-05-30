# coding=utf-8
# Author: Jianghan LI
# Question: 599.Minimum_Index_Sum_of_Two_Lists
# Date: 2017-05-30 13:28 - 13:43, 0 wrong try


class Solution(object):

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = dict((v, i) for i, v in enumerate(list1))
        res = collections.defaultdict(list)
        for i, v in enumerate(list2):
            if v in d:
                res[i + d[v]].append(v)
        return res[min(res.keys())]

    def findRestaurant(self, list1, list2):
        d1 = {v: i for i, v in enumerate(list1)}
        d2 = {v: i for i, v in enumerate(list2)}
        d = collections.defaultdict(list)
        for r in set(list1) & set(list2):
            d[(d1[r] + d2[r])].append(r)
        return d[min(d.keys())]


s = Solution()
print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
