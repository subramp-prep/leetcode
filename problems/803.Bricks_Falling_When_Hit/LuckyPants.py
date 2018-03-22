class Solution:

    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])

        # Connect unconnected bricks and
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += dfs(i - 1, j)
            ret += dfs(i + 1, j)
            ret += dfs(i, j - 1)
            ret += dfs(i, j + 1)
            return ret

        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            ret = False
            ret |= (h[0] - 1 >= 0 and grid[h[0] - 1][h[1]] == 2)
            ret |= (h[0] + 1 < m and grid[h[0] + 1][h[1]] == 2)
            ret |= (h[1] - 1 >= 0 and grid[h[0]][h[1] - 1] == 2)
            ret |= (h[1] + 1 < n and grid[h[0]][h[1] + 1] == 2)
            ret |= (h[0] == 0)
            return ret

        # Mark whether there is a brick at the each hit
        for h in hits:
            if grid[h[0]][h[1]] == 1:
                grid[h[0]][h[1]] = 0
            else:
                grid[h[0]][h[1]] = -1

        # Get grid after all hits
        for i in range(n):
            dfs(0, i)

        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0] * len(hits)
        for i in reversed(range(len(hits))):
            h = hits[i]
            if grid[h[0]][h[1]] == -1:
                continue
            grid[h[0]][h[1]] = 1
            if not is_connected(h[0], h[1]):
                continue
            ret[i] = dfs(h[0], h[1]) - 1

        return ret


# https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-bricks/119285?page=1

# We can reverse the problem and count how many new no-dropping bricks are
# added when we add the bricks reversely. It’s just the same of counting
# dropping bricks when erase one brick.

# Let m, n = len(grid), len(grid[0]).

# Here is the detailed solution:

# For each hit (i, j), if grid[i][j]==0, set grid[i][j]=-1 otherwise set grid[i][j]=0. Since a hit may happen at an empty position, we need to seperate emptys from bricks.
# For i in [0, n], do dfs at grid[i][0] and mark no-dropping bricks. Here we get the grid after all hits.
# Then for each hit (i,j) (reversely), first we check grid[i][j]==-1, if yes, it’s empty, skip this hit. Then we check whether it’s connected to any no-dropping bricks or it’s at the top, if not, it can’t add any no-dropping bricks, skip this hit. Otherwise we do dfs at grid[i][j], mark new added no-dropping bricks and record amount of them.
# Return the amounts of new added no-dropping bricks at each hits.


# Improved by li to li.py
