class Solution(object):

    def updateMatrix(self, A):
        A = [[10000 * x for x in r] for r in A]
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        q = collections.deque([(r, c, 0)
                               for r in xrange(R)
                               for c in xrange(C)
                               if A[r][c] == 0])
        while q:
            r, c, depth = q.popleft()
            for cr, cc in neighbors(r, c):
                if A[cr][cc] > depth + 1:
                    A[cr][cc] = depth + 1
                    q.append((cr, cc, depth + 1))
        return A

# https://discuss.leetcode.com/topic/83482/python-simple-with-explanation/2
# improved
