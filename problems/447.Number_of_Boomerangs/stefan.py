def numberOfBoomerangs(self, points):
    return sum(
        n * (n - 1)
        for x1, y1 in points
        for n in collections.Counter(
            (x1 - x2) ** 2 + (y1 - y2) ** 2
            for x2, y2 in points).values())