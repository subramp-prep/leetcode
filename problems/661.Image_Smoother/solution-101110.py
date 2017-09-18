class Solution(object):

    # modified by Li
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M:
            return []
        m, n = len(M), len(M[0])
        res = copy.deepcopy(M)
        for x in range(m):
            for y in range(n):
                neighbors = [M[i][j] for i in (x - 1, x, x + 1) for j in (y - 1, y, y + 1)
                             if 0 <= i < m and 0 <= j < n]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res
