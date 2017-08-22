# coding=utf-8
# Author: Jianghan LI
# Question: 318.Maximum_Product_of_Word_Lengths
# Complexity: O(N)
# Date: 2017-08-21 10:47 - 11:27

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            key = tuple(set(w))
            d[key] =  max(d.get(key,0),len(w))
        return max((0 if set(a) & set(b) else d[a]*d[b]) for a in d for b in d) if words else 0


# letters + set + hashable = 26 bits
# hashtable的key可以用bit来做