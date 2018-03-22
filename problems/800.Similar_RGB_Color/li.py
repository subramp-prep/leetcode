# coding=utf-8
# Author: Jianghan LI
# Question: 800.Similar_RGB_Color
# Complexity: O(1)
# Date: 2018-03-17 0:00:00 - 0:16:43, 0 wrong try


class Solution:

    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def to10(c):
            if c.isdigit():
                return int(c)
            return ord(c) - ord('a') + 10

        def to16(x):
            if x < 10:
                return str(x)
            return ['a', 'b', 'c', 'd', 'e', 'f'][x - 10]

        def similar(x):
            a, b = to10(x[0]), to10(x[1])
            res = a * 17
            value = (a * 16 + b)
            if a < 16 and abs((a + 1) * 17 - value) < abs(value - res):
                res = (a + 1) * 17
            if a > 0 and abs((a - 1) * 17 - value) < abs(value - res):
                res = (a - 1) * 17
            return to16(res / 17) * 2
        return '#' + similar(color[1:3]) + similar(color[3:5]) + similar(color[5:])

    def similarRGB(self, c):
        def similar(x):
            a, b = int(x[0], 16), int(x, 16)
            res = min([a - 1, a, a + 1], key=lambda i: abs(b - i * 17))
            return hex(res)[2] * 2
        return '#' + similar(c[1:3]) + similar(c[3:5]) + similar(c[5:])

    # 除以17
    def similarRGB(self, c):
        def similar(x):
            return hex(int(round(int(x, 16) / 17.0)))[2] * 2
        return '#' + similar(c[1:3]) + similar(c[3:5]) + similar(c[5:])

############ test case ###########
s = Solution()
print s.similarRGB("#09f166")  # #11ee66
print s.similarRGB("#00fe66")  # #00ff66
