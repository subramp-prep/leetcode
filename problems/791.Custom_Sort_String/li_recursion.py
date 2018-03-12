class Solution(object):
    D = {0: 1, 1: 1, 2: 2}
    T = {0: 1, 1: 0, 2: 1}

    def numTilings(self, N):
        return self.getD(N) % (10**9 + 7)

    def getD(self, N):
        if N in self.D:
            return self.D[N]
        self.D[N] = (self.getD(N - 1) + self.getD(N - 2) + self.getT(N - 1) * 2) % (10**9 + 7)
        return self.D[N]

    def getT(self, N):
        if N in self.T:
            return self.T[N]
        self.T[N] = (self.getT(N - 2) + self.getT(N - 1)) % (10**9 + 7)
        return self.T[N]
