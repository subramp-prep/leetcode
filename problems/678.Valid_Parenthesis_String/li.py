# coding=utf-8
# Author: Jianghan LI
# Question: 678.Valid_Parenthesis_String
# Complexity: O(N)
# Date: 2017-09-17
# Contest50 0:37:28 － 0:41:26, 1 wrong try

class Solution(object):

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin -= 1
            if i == '*':
                cmax += 1
                cmin -= 1
            if cmax == 0:
                cmin = 0
            if cmax < 0:
                return False
            # print cmax,cmin
        if cmin > 0:
            return False

        s = s[::-1]
        cmin = cmax = 0
        for i in s:
            if i == ')':
                cmax += 1
                cmin += 1
            if i == '(':
                cmax -= 1
                cmin -= 1
            if i == '*':
                cmax += 1
                cmin -= 1
            if cmax == 0:
                cmin = 0
            if cmax < 0:
                return False
            # print cmax,cmin
        if cmin > 0:
            return False
        else:
            return True

    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            cmax = cmax-1 if i==")" else cmax+1
            cmin = cmin+1 if i=='(' else max(cmin - 1, 0)
            if cmax < 0: return False
        return cmin == 0



############ test case ###########
s = Solution()
print s.checkValidString("()")
print s.checkValidString("(*)")
print s.checkValidString("(*))")
print s.checkValidString("((*))((*")


############ comments ############
# https://discuss.leetcode.com/topic/103984/python-easy-understand-solution

# The number of open parenthesis is in a range [cmin, cmax]
# cmax counts the maximum open parenthesis.
# cmin counts the minimum open parenthesis.
# The string is valid for 2 condition:

# cmax will never be negative.
# cmin is 0 at the end.