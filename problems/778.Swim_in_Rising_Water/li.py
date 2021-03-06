# coding=utf-8
# Author: Jianghan LI
# Question: 778.Swim_in_Rising_Water
# Complexity: O(N^2logN)
# Date: 2018-02-09


class Solution(object):

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        l, r = grid[0][0], N * N - 1

        def reachable(T):
            bfs = [(0, 0)]
            seen = set([(0, 0)])
            for x, y in bfs:
                if grid[x][y] <= T:
                    if x == y == N - 1:
                        return True
                    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= x + i < N and 0 <= y + j < N and (x + i, y + j) not in seen:
                            seen.add((x + i, y + j))
                            bfs.append((x + i, y + j))
            return False

        while l < r:
            m = (l + r) / 2
            if reachable(m):
                r = m
            else:
                l = m + 1
        return r


############ test case ###########
s = Solution()
print s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14,
                                                            15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])
# 11
print s.swimInWater([[11, 15, 3, 2], [6, 4, 0, 13], [5, 8, 9, 10], [1, 14, 12, 7]])

# 16
print s.swimInWater([[105, 209, 171, 91, 64, 394, 279, 11, 45, 84, 207, 321, 216, 197, 381, 377, 78, 19, 203, 198], [141, 10, 335, 170, 265, 104, 338, 40, 397, 376, 346, 356, 212, 154, 280, 177, 247, 90, 87, 360], [99, 59, 242, 149, 344, 172, 276, 230, 133, 193, 284, 345, 46, 363, 30, 142, 295, 70, 224, 200], [251, 88, 379, 72, 319, 272, 243, 165, 180, 182, 387, 264, 23, 67, 137, 342, 125, 139, 144, 367], [94, 211, 151, 37, 290, 112, 343, 157, 300, 271, 260, 373, 369, 294, 289, 57, 44, 12, 20, 340], [220, 368, 186, 277, 181, 187, 273, 214, 315, 337, 328, 18, 231, 223, 331, 75, 275, 96, 135, 150], [202, 74, 27, 184, 399, 341, 49, 62, 261, 86, 314, 383, 302, 257, 61, 148, 268, 120, 36, 25], [15, 253, 285, 185, 226, 146, 126, 122, 83, 361, 110, 234, 183, 239, 52, 190, 152, 81, 136, 188], [39, 199, 358, 26, 301, 116, 32, 386, 29, 138, 393, 159, 102, 140, 370, 227, 282, 111, 5, 33], [189, 35, 132, 54, 210, 235, 28, 353, 281, 127, 318, 58, 100, 286, 384, 24, 307, 252, 80, 103], [244, 176, 124, 79, 161, 355, 218, 398, 392, 380, 225, 121, 178, 352, 329, 322, 167, 51, 313, 85], [107, 118, 351, 287, 324, 283, 48, 320, 82, 364, 357, 16, 219, 330, 89, 143, 241, 262, 71, 191], [95, 97, 3, 7, 270, 249, 213, 339, 362, 298, 4, 258, 248, 390, 299, 306, 156, 164, 109, 229], [221, 9, 228, 160, 274, 263, 374, 147, 98, 63, 13, 41, 326, 396, 349, 372, 385, 317, 325, 266], [53, 131, 173, 312, 174, 114, 250, 119, 163, 22, 246, 92, 278, 365, 292, 215, 14, 304, 204, 73], [233, 323, 366, 130, 378, 305, 311, 93, 134, 217, 297, 327, 232, 194, 240, 1, 208, 6, 310, 47], [69, 101, 332, 195, 254, 236, 50, 166, 56, 168, 267, 17, 359, 347, 65, 316, 238, 296, 348, 222], [76, 123, 129, 293, 391, 2, 245, 108, 303, 38, 66, 55, 43, 256, 162, 60, 179, 77, 336, 21], [196, 388, 333, 395, 42, 382, 291, 237, 288, 375, 128, 145, 192, 158, 350, 259, 206, 34, 334, 255], [201, 175, 153, 68, 205, 155, 115, 269, 389, 169, 371, 308, 117, 31, 354, 8, 113, 309, 106, 0]])

# 266
