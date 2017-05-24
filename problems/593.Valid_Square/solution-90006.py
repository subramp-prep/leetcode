class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        return len({(a[0] - b[0])**2 + (a[1] - b[1])**2 for a in points for b in points}) == 3 and \
            len(set(map(tuple, points))) == 4

    def validSquare(self, *p):
        return len(set((a[0] - b[0])**2 + (a[1] - b[1])**2 for a in p for b in p)) == 3 and len(set(map(tuple, p))) == 4
