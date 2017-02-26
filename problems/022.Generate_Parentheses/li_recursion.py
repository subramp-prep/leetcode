# coding=utf-8
# Author: Jianghan LI
# Question: User
# Date: 15/02/2017 10:57-


class Solution(object):

    def generateParenthesis(self, n, left=0, right=0, cur=''):
        """
        :type n: int
        :rtype: List[str]
        """
        if left == n:
            return [cur + ')' * (n - right)]
        if left == right:
            return self.generateParenthesis(n, left + 1, right, cur + '(')
        return self.generateParenthesis(n, left + 1, right, cur + '(') \
            + self.generateParenthesis(n, left, right + 1, cur + ')')
s = Solution()
print s.generateParenthesis(3)

# 同样三种情况，用recursion。改变原函数
