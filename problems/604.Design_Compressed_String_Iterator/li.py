# coding=utf-8
# Author: Jianghan LI
# Question: 604.Design_Compressed_String_Iterator
# Date: 2017-06-12


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s, self.n, self.i = compressedString, 0, 0

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        self.n -= 1
        return self.c

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.n:
            return True
        if self.i == len(self.s):
            return False
        self.c = self.s[self.i]
        start = self.i = self.i + 1
        while self.i < len(self.s) and '0' <= self.s[self.i] <= '9':
            self.i += 1
        self.n = int(self.s[start:self.i])
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
