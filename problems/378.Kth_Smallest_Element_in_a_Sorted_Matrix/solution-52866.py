import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        return list(heapq.merge(*matrix))[k-1]