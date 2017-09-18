# coding=utf-8
# Author: Jianghan LI
# Question: 599.Minimum_Index_Sum_of_Two_Lists
# Complexity: O(N)
# Date: 2017-08-31 10:21 - 10:30, 0 wrong try

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {v:i for i,v in enumerate(list1)}
        d2 = {v:i for i,v in enumerate(list2)}
        for v in d1: d1[v] += d2.get(v, float('inf'))
        index = min(d1.values())
        return [v for v in d1 if d1[v] == index]

    #just shoter
    def findRestaurant(self, list1, list2):
        d1 = {v:i for i,v in enumerate(list1)}
        d2 = {v:i for i,v in enumerate(list2)}
        index = min(d1[v] + d2[v] for v in d1 if v in d2)
        return [v for v in d1 if v in d2 and d2[v] + d1[v] == index]

############ test case ###########
s = Solution()
print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])


############ comments ############

