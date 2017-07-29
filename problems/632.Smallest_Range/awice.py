import collections
import heapq
import time


class Solution(object):

    def smallestRange(self, A):
        A = [row[::-1] for row in A]
        ans = -1e9, 1e9
        for left in sorted(reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans

    # li, not reverse A
    def smallestRange(self, A):
        ans = -1e9, 1e9
        for right in sorted(set(x for l in A for x in l))[::-1]:
            for B in A:
                while B and right < B[-1]:
                    B.pop()
                if not B:
                    return ans
            left = min(B[-1] for B in A)
            if right - left <= ans[1] - ans[0]:
                ans = left, right
        return ans

    #li, not pop
    def smallestRange3(self, A):
        ans = -1e9, 1e9
        k = len(A)
        pos = [0] * k
        for left in sorted(set(x for l in A for x in l)):
            for i in range(k):
                while pos[i] < len(A[i]) and A[i][pos[i]] < left:
                    pos[i] += 1
                if pos[i] == len(A[i]):
                    return ans
            right = max(A[i][pos[i]] for i in range(k))
            if right - left <= ans[1] - ans[0]:
                ans = left, right
        return ans


############ test case ###########
s = Solution()
A = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]] * 50000


B = [[e for e in a] for a in A]
start = time.time()
print s.smallestRange(B)
print(time.time() - start)

B = [[e for e in a] for a in A]
start = time.time()
print s.smallestRange2(B)
print(time.time() - start)

B = [[e for e in a] for a in A]
start = time.time()
print s.smallestRange3(B)
print(time.time() - start)
