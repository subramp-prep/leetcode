# coding=utf-8
# Author: Han
# Question: 173.Binary_Search_Tree_Iterator
# Date: 2017-06-01
# Complexity: O(logN) Space，O(N) Time


class BSTIterator(object):

    def __init__(self, root):
        self.stack, self.cur = [], root

    def hasNext(self):
        return self.stack or self.cur

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        next = self.stack.pop()
        self.cur = next.right
        return next.val
