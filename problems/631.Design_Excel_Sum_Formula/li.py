# coding=utf-8
# Author: Jianghan LI
# Question: 631.Design_Excel_Sum_Formula
# Date: 17:04 - 17:44
# Complexity: O(N)


import collections


class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        self.M[r - 1][ord(c) - 65]['v'] = v
        self.M[r - 1][ord(c) - 65]['sum'] = None

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        if not self.M[r - 1][ord(c) - 65]['sum']:
            return self.M[r - 1][ord(c) - 65]['v']
        ret = 0
        for (i, j), t in self.M[r - 1][ord(c) - 65]['sum'].items():
            ret += self.get(i, j) * t
        return ret

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    def parse(self, strs):
        c = collections.Counter()
        for s in strs:
            if ':' in s:
                s, e = s.split(':')
                i1, j1 = int(s[1:]), ord(s[0]) - 64
                i2, j2 = int(e[1:]), ord(e[0]) - 64
                for i in range(i1, i2 + 1):
                    for j in range(j1, j2 + 1):
                        c[(i, chr(j + 64))] += 1
            else:
                i, j = int(s[1:]), s[0]
                c[(i, j)] += 1
        return c


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
