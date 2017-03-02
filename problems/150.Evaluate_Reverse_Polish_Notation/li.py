# coding=utf-8
# Author: Han
# Question: 127.Word_Ladder
# Date: 02/03/2017
# O(N) stack


class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in '+-*/':
                if i == '+':
                    stack[-1] = stack[-2] + stack.pop()
                if i == '-':
                    stack[-1] = stack[-2] - stack.pop()
                if i == '*':
                    stack[-1] = stack[-2] * stack.pop()
                if i == '/':
                    stack[-1] = int(float(stack[-2]) / stack.pop())
            else:
                stack.append(int(i))
        return stack[0]
