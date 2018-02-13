# Edited by Li
class Solution(object):

    def canWin(self, m, desired, cur, d):
        if cur in d:
            return d[cur]
        for i in range(m):
            if (cur >> i) & 1 == 0:
                if i + 1 >= desired or not self.canWin(m, desired - (i + 1), cur + (1 << i), d):
                    d[cur] = True
                    return d[cur]
        d[cur] = False
        return d[cur]

    def canIWin(self, m, desired):
        if (m + 1) * m / 2 < desired:
            return False
        return self.canWin(m, desired, 0, {})
