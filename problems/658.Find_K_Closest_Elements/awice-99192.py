def findClosestElements(self, A, K, X):
    return sorted(sorted(A, key=lambda y: (abs(X - y), y))[:K])
