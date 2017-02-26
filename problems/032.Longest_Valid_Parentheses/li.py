# coding=utf-8
# Author: Jianghan LI
# Question: 032.Longest_Valid_Parentheses/li.py
# Date: 19/02/2017 17:16-17:59


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = cur = left = right = 0
        while right < len(s):
            cur += 1 if s[right] == '(' else -1
            right += 1
            if cur == 0:
                res = max(res, right - left)
            while cur < 0:
                cur += -1 if s[left] == '(' else 1
                left += 1
        s = s[::-1]
        cur = left = right = 0
        while right < len(s):
            cur += 1 if s[right] == ')' else -1
            right += 1
            if cur == 0:
                res = max(res, right - left)
            while cur < 0:
                cur += -1 if s[left] == ')' else 1
                left += 1
        return res

    def longestValidParentheses2(self, s):
        res = cur = 0
        left = -1
        for right in range(len(s)):
            cur += 1 if s[right] == '(' else -1
            if cur == 0:
                res = max(res, right - left)
            if cur < 0:
                cur, left = 0, right

        cur, right = 0, len(s)
        for left in range(len(s))[::-1]:
            cur += 1 if s[left] == ')' else -1
            if cur == 0:
                res = max(res, right - left)
            if cur < 0:
                cur, right = 0, left
        return res

    def longestValidParentheses3(self, s):
        res = h = l = 0  # result, height, current length
        for c in s:
            h += 1 if c == '(' else -1
            l += 1
            if h == 0:
                res = max(res, l)
            if h < 0:
                h = l = 0
        h = l = 0
        for c in s[::-1]:
            h += 1 if c == ')' else -1
            l += 1
            if h == 0:
                res = max(res, l)
            if h < 0:
                h = l = 0
        return res

s = Solution()

print s.longestValidParentheses3('(()')
print s.longestValidParentheses3("()(()")

# longestValidParentheses 这是我第一遍AC的代码，从左到右，从右到左。
# 开始只想扫一遍，后来发现(()这种尾部情况没有计算到，也不太好处理.
# 着急AC然后我就干脆复制一遍代码，左右对称的再来一遍。这是我的思路
# 一开始就觉得不用额外的空间，看到stack的做法还挺巧妙的。
# 相当于方便的记录了有用的index，和找到match的左括号

# longestValidParentheses2 根据AC_stack_n.cpp改进的,同时使用dp和stack。
# longestValidParentheses3 是想到 记录index或left其实是为了计算当前长度，其实没有必要。
