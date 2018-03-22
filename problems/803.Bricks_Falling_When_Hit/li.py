class Solution:

    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])

        # Connect unconnected bricks and
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return ret

        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            ret = (i - 1 >= 0 and grid[i - 1][j] == 2)
            ret |= (i + 1 < m and grid[i + 1][j] == 2)
            ret |= (j - 1 >= 0 and grid[i][j - 1] == 2)
            ret |= (j + 1 < n and grid[i][j + 1] == 2)
            ret |= (i == 0)
            return ret

        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1

        # Get grid after all hits
        for j in range(n):
            dfs(0, j)

        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0] * len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                ret[k] = dfs(i, j) - 1
        return ret


############ test case ###########
s = Solution()

# print s.hitBricks([[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]])  # [1, 0, 1, 0, 0]
# print s.hitBricks([[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]])  # [0,0,1,0]
# print s.hitBricks([[1, 1, 1], [1, 1, 1]], [[1, 0], [1, 1], [1, 2]])  # [0,0,1,0]
print s.hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]])  # [0,3,0]


############ comments ############
# Improved from LuckyPants
