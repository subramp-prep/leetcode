# coding=utf-8
# Author: Jianghan LI
# Question: 554.Brick_Wall
# Complexity: O(N)
# Date: 2017-07-31 11:21 - 11:28, 1 wrong try


class Solution(object):

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        c = collections.Counter()
        for row in wall:
            cur = 0
            for brick in row[:-1]:
                cur += brick
                c[cur] += 1
        return len(wall) - c.most_common(1)[0][1] if c else len(wall)

    def leastBricks(self, wall):
        for row in wall:
            for i in range(1, len(row)):
                row[i] += row[i - 1]
        c = collections.Counter(i for row in wall for i in row[:-1])
        return len(wall) - max(c.values() + [0])


# wrong try: [[1],[1],[1]]时counter为空，most_common异常。
