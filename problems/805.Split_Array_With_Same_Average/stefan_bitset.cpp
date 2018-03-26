// C++ version using bitset<300001>

// Sadly bitset doesn’t support dynamic sizes.
// So I must make it as large as the largest possible sum,
// not just as large as the sum of the given input and
// not just as large as the current prefix sum of the given input.
// It takes about 190 ms,
// much slower than my bitset over size version (which takes about 35 ms).
// I could make it about twice as fast by not going the full N-range
// for every a but only going as far as how many a values I’ve used so far,
// but meh… what’s the point if it’s gonna be slower anyway.

bool splitArraySameAverage(vector < int > & A) {
    int N = A.size(), S = 0
    for (int a: A) S += a
    bitset < 300001 > p[N] = {1}
    for (int a: A)
    for (int n=N - 2
         n >= 0
         n - -)
    p[n + 1] |= p[n] << a
    for (int n=1
         n < N
         n + +)
    if (S * n % N == 0 & &  p[n][S * n / N])
    return true
    return false
}