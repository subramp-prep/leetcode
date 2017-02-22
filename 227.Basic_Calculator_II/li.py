# coding=utf-8
# Author: Jianghan LI
# Question: 227.Basic_Calculator_II/li.py
# Date: 22/02/2017 21:13-21:25


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = i = tmp = 0
        s = '+' + ''.join(s.split(' '))
        while i < len(s):
            op = s[i]
            cur = ''
            i += 1
            while i < len(s) and '0' <= s[i] <= '9':
                cur += s[i]
                i += 1
            if op == '+':
                res += tmp
                tmp = int(cur)
            elif op == "-":
                res += tmp
                tmp = -int(cur)
            elif op == "*":
                tmp *= int(cur)
            elif op == "/":
                tmp = int(tmp / float(cur))
        return res + tmp

############ test case ###########
s = Solution()
print s.calculate("1+2+3")

############ comments ############
# O(n) O(1)
# 把原字符串中空格替换掉，在前面加上＋。
# 这样字符串变成符号加数字
# res存最终结果
# tmp表示当前乘除法计算出的数
# cur表示当前读的数
