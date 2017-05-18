def findUnsortedSubarray(self, A):
    B = sorted(A)
    if A == B:
        return 0
    for i in xrange(len(A)):
        if A[i] != B[i]:
            break
    for j in xrange(len(A) - 1, -1, -1):
        if A[j] != B[j]:
            break
    return j - i + 1
