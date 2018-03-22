class Solution(object):

    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n_bricks = sum(map(sum, grid))
        for hit in hits:
            grid, n_bricks, drop = self.hitBrick(grid, hit, n_bricks)
            res.append(drop)
        return res

    def hitBrick(self, grid, hit, n_bricks):
        if grid[hit[0]][hit[1]] == 0:
            return grid, n_bricks, 0
        grid[hit[0]][hit[1]] = 0
        if self.connected(grid, hit[0], hit[1]):
            return grid, n_bricks - 1, 0
        M, N = len(grid), len(grid[0])
        left = [grid[0]] + [[0] * N for _ in range(M - 1)]
        bfs = [(0, y) for y in range(N) if grid[0][y]]
        for x, y in bfs:
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x1, y1 = x + i, y + j
                if self.valid(grid, x1, y1) and left[x1][y1] == 0:
                    bfs.append((x + i, y + j))
                    left[x1][y1] = 1
        drop = n_bricks - len(bfs) - 1
        return left, len(bfs), drop

    def valid(self, grid, x, y):
        M, N = len(grid), len(grid[0])
        return 0 <= x < M and 0 <= y < N and grid[x][y]

    def connected(self, grid, x, y):
        if self.valid(grid, x - 1, y) and \
                self.valid(grid, x, y + 1) and \
                not self.valid(grid, x + 1, y) and \
                not self.valid(grid, x, y - 1):
            return self.valid(grid, x - 1, y + 1)

        if self.valid(grid, x - 1, y) and \
                not self.valid(grid, x, y + 1) and \
                not self.valid(grid, x + 1, y) and \
                self.valid(grid, x, y - 1):
            return self.valid(grid, x - 1, y - 1)

        if self.valid(grid, x - 1, y) + \
                self.valid(grid, x, y + 1) + \
                self.valid(grid, x + 1, y) + \
                self.valid(grid, x, y - 1) == 1:
            return x > 0
        return False


############ test case ###########
s = Solution()

# print s.hitBrick(grid=[[1, 0, 0, 0], [1, 1, 1, 0]], hit=[1, 0])
# print s.hitBricks(grid=[[1, 0, 0, 0], [1, 1, 1, 0]], hits=[[1, 0]])
# print s.hitBricks(grid=[[1, 0, 0, 0], [1, 1, 0, 0]], hits=[[1, 1], [1, 0]])

# print s.hitBricks([[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]])  # [1, 0, 1, 0, 0]
# print s.hitBricks([[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]])  # [0,0,1,0]
# print s.hitBricks([[1, 1, 1], [1, 1, 1]], [[1, 0], [1, 1], [1, 2]])  # [0,0,1,0]
print s.hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]])  # [0,0,1,0]
