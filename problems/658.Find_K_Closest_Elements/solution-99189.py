def findClosestElements(self, arr, k, x):
    return sorted([n for d, n in sorted([(abs(n - x), n) for n in arr])[:k]])
