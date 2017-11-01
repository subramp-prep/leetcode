def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))


# Since there are no lakes, every pair of neighbour cells with different
# values is part of the perimeter (more precisely, the edge between them
# is). So just count the differing pairs, both horizontally and vertically
# (for the latter I simply transpose the grid).
