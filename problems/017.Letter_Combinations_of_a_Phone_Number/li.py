# coding=utf-8
# Author: Jianghan LI
# Question: 017.Letter_Combinations_of_a_Phone_Number
# Date: 2017-07-10
# Complexity: O(4^N)


import itertools


class Solution(object):
    l = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return list(''.join(w) for w in itertools.product(*(self.l[int(i) - 2] for i in digits)) if w)


############ test case ###########
s = Solution()
print s.letterCombinations('23')
print s.letterCombinations('')

############ comments ############
