# coding=utf-8
# Author: Jianghan LI
# Question: 635.Design_Log_Storage_System
# Date: 2017-07-05 10:14 - 10:31, 1 wrong try
# Complexity: O(1) O(1) O(N)

import collections


class LogSystem(object):

    def __init__(self):
        self.c = collections.defaultdict(list)
        self.i = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.c[timestamp].append(id)

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        i = self.i[gra]
        s = s[:i] + "0000:00:00:00:00:00"[i:]
        e = e[:i] + "9999:99:99:99:99:99"[i:]
        ret = []
        for t, ids in self.c.items():
            if s <= t <= e:
                ret.extend(ids)
        return ret


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

############ test case ###########
s = LogSystem()
# operations = ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
# inputs = [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], [
#     "2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
operations = ["LogSystem", "put", "put", "retrieve"]
inputs = [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:23:59:59"],
          ["2017:01:01:23:59:59", "2017:01:02:23:59:59", "Second"]]

for i in range(1, len(inputs)):
    print eval("s." + operations[i])(*inputs[i])

############ comments ############
# Wrong try: for gra == "Second", s <= t <= e insted of just s < t < e
