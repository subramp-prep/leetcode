class Solution(object):

    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find_region(grid):
            index = 0
            seen = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if not seen[i][j]:
                        seen[i][j] = 1
                        if grid[i][j] > 0:
                            index += 1
                            bfs(seen, i, j, index)

            return index

        def bfs(seen, i, j, index):
            bfs_list = [[i, j]]
            for x, y in bfs_list:
                if grid[x][y] > 0:
                    grid[x][y] = index
                    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        if 0 <= x + dx < m and 0 <= y + dy < n and seen[x + dx][y + dy] == 0:
                            seen[x + dx][y + dy] = 1
                            bfs_list.append([x + dx, y + dy])

        def will_infect(grid):
            c = collections.Counter()
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 0:
                        virus = set(grid[x + dx][y + dy] for dx, dy in [[1, 0], [0, 1], [-1, 0],
                                                                        [0, -1]] if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] > 0)
                        c += collections.Counter(virus)
            return c

        def set_walls(grid, index):
            res = 0
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == index:
                        grid[x][y] = -1
                        res += sum(1 for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]] if 0 <=
                                   x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 0)
            return res

        def spread(grid):
            grid2 = [[x for x in line] for line in grid]
            for x in range(m):
                for y in range(n):
                    if grid[x][y] > 0:
                        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 0:
                                grid2[x + dx][y + dy] = grid[x][y]
            return grid2

        m, n, res = len(grid), len(grid[0]), 0
        while True:
            find_region(grid)
            c = will_infect(grid)
            if not c:
                break
            index = c.most_common(1)[0][0]
            res += set_walls(grid, index)
            grid = spread(grid)
        return res
