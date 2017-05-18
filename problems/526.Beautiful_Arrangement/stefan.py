def countArrangement(self, N):
    def count(i, X, memo={}):
        if i < 2:
            return 1
        if X not in memo:
            memo[X] = sum(count(i - 1, X - {x})
                          for x in X
                          if x % i == 0 or i % x == 0)
        return memo[X]
    return count(N, frozenset(range(1, N + 1)))
