# coding=utf-8
# Author: Jianghan LI
# Question: 460.LFU_Cache
# Date: 2017-06-21
import time


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.d = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        self.d[key][0] += 1
        self.d[key][1] = time.time()
        return self.d[key][3]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.c == 0:
            return
        if key in self.d:
            self.d[key] = [self.d[key][0] + 1, time.time(), key, value]
            return
        if len(self.d) == self.c:
            least = min(self.d[i] for i in self.d)
            del self.d[least[2]]
        self.d[key] = [0, time.time(), key, value]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# wrong try: the case that capacity = 0
