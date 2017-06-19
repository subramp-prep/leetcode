class Solution(object):

    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        m = len(arrays)
        MAX, max_i = max([(arrays[i][-1], i) for i in range(m)])
        MIN, min_i = min([(arrays[i][0], i) for i in range(m)])
        a = max(abs(arrays[i][0] - MAX) for i in range(m) if i != max_i)
        b = max(abs(arrays[i][-1] - MIN) for i in range(m) if i != min_i)
        return max(a, b)

    # Jianghan version
    def maxDistance(self, arrays):
        MAX, max_i = max([(l[-1], i) for i, l in enumerate(arrays)])
        MIN, min_i = min([(l[0], i) for i, l in enumerate(arrays)])
        SMAX = max(l[-1] for i, l in enumerate(arrays) if i != max_i)
        SMIN = min(l[0] for i, l in enumerate(arrays) if i != min_i)
        return MAX - MIN if max_i != min_i else max(MAX - SMIN, SMAX - MIN)

s = Solution()
print s.maxDistance([[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]])
