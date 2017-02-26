class Solution(object):

  def isRectangleCover(self, rectangles):
    def recordCorner(point):
      if point in corners:
        corners[point] += 1
      else:
        corners[point] = 1

    corners = {}                                # record all corners
    L, B, R, T, area = float('inf'), float(
        'inf'), -float('inf'), -float('inf'), 0

    for sub in rectangles:
      L, B, R, T = min(L, sub[0]), min(
          B, sub[1]), max(R, sub[2]), max(T, sub[3])
      ax, ay, bx, by = sub[:]
      # sum up the area of each sub-rectangle
      area += (bx - ax) * (by - ay)
      map(recordCorner, [(ax, ay), (bx, by), (ax, by), (bx, ay)])

    if area != (T - B) * (R - L):
      return False        # check the area

    big_four = [(L, B), (R, T), (L, T), (R, B)]

    for bf in big_four:                         # check corners of big rectangle
      if bf not in corners or corners[bf] != 1:
        return False

    for key in corners:                         # check existing "inner" points
      if corners[key] % 2 and key not in big_four:
        return False

    return True


s = Solution()
rectangles = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [3, 2, 4, 4],
    [1, 3, 2, 4],
    [2, 3, 3, 4]
]
print s.isRectangleCover(rectangles)
