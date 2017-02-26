# coding=utf-8
# Author: Jianghan LI
# Question: User
# Date: 15/02/2017 09:57-10:09


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dfsList = [(n, n, '')]
        res = []
        while len(dfsList):
            left, right, cur = dfsList.pop()
            if left:
                dfsList.append((left - 1, right, cur + '('))
                if left < right:
                    dfsList.append((left, right - 1, cur + ')'))
            else:
                res.append(cur + ')' * right)
        return res

s = Solution()
print s.generateParenthesis(3)
# dfsLift中每一个元素是(左括号剩余，右括号剩余，当前已构建的字符串)
# 有三种情况需要考虑：
# 1. left==right，下一个必须插入左括号
# 2. left==0，插入剩余所有右括号
# 3. left<right 可插入右括号
