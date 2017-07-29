# Going through all permutations of the digits, returning the first one
# that's larger than the input (unless it's out of range). Pretty
# inefficient but gets accepted in about 200 ms...


def nextGreaterElement(self, n):
    n = tuple(str(n))
    p = int(''.join(next((p for p in itertools.permutations(sorted(n)) if p > n), '9' * 10)))
    return p if p < 2**31 else -1

# The worst case is n = 1111111111, because I go through all 10!
# permutations and each one gets fully compared. This case takes about 600
# ms.
