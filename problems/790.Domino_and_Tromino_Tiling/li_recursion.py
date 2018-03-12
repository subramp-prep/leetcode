class Solution(object):
    T = {0: 0, 1: 0, 2: 1}
    D = {0: 1, 1: 1, 2: 2}

    def getD(self, N):
        if N in self.D:
            return self.D[N]
        self.D[N] = (self.getD(N - 1) + self.getD(N - 2) + self.getT(N - 1) * 2) % (10**9 + 7)
        return self.D[N]

    def getT(self, N):
        if N in self.T:
            return self.T[N]
        self.T[N] = (self.getD(N - 2) + self.getT(N - 1)) % (10**9 + 7)
        return self.T[N]

    numTilings = getD


############ test case ###########
s = Solution()
print s.numTilings(1)  # 1
print s.numTilings(2)  # 2
print s.numTilings(3)  # 5
print s.numTilings(10)  # 1255
print s.numTilings(30)  # 312342182
