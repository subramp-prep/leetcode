# coding=utf-8
# Author: Jianghan LI
# Question: 677.Map_Sum_Pairs
# Complexity: O(N)
# Date: 2017-09-17
# Contest50 0:00:00 － 0:06:40, 0 wrong try
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum(self.d[i] for i in self.d if i.startswith(prefix))



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


############ comments ############
# https://discuss.leetcode.com/topic/103983/python-easy-and-concise-3-lines-solution
