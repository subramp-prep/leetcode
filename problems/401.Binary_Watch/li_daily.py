# Han, Python 35ms beats 99%
# Brute Force


class Solution(object):
    dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    for h in range(12):
        for m in range(60):
            dict[(bin(h) + bin(m)).count('1')].append('%d:%02d' % (h, m))

    def readBinaryWatch(self, num):
        return self.dict.get(num, [])
