class Solution(object):

    def hIndex(self, cita):
        return sum(i < j for i, j in enumerate(sorted(cita, reverse=True)))
