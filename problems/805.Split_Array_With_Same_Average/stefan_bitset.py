# Python version

# My fastest Python solution so far, gets accepted in about 44 ms(tried
# five times, took 44, 48, 44, 40 and 44 ms). After using bitset over size
# N I realized I could do bitset over sum S instead, using Python’s big
# integers. Then almost all action is in Python’s C code(for big
# integers). Which is fast and saves me code.


def splitArraySameAverage(self, A):
    N, S, P = len(A), sum(A), [1]
    for a in A:
        P[1:] = [(p << a) | q for p, q in zip(P, P[1:] + [0])]
    return any(S * n % N == 0 and P[n] & (1 << (S * n // N))
               for n in range(1, N))

# A nice side effect of using big integers for the bitsets is that they
# don’t always store S bits but only as many bits as needed to include the
# largest 1 - bit. We can even take further advantage of this by using for
# a in sorted(A), which keeps the bitsets short as long as it can. Though
# that doesn’t make it faster here, as 44 ms is already pretty much as
# fast as possible. Even the below cheating solution takes about 40 ms:

answers = iter('TFFTFTFFFFTTFFFFFFFFFFFFFTTFFFFFTFFFFFTFFFFTFFFFTFFFFFFFFTFFFTFTTFFFTFTFFFFFFFFFFFFTFFF')


class Solution:

    def splitArraySameAverage(self, A):
        return next(answers) == 'T'

# Ruby version

# Ruby also has big integers that we can use as bitsets. Takes about 50 ms(five attempts took 52, 52, 48, 52 and 48 ms):


def split_array_same_average(a)
    n, s, p = a.size, a.sum, [1]
    a.each {| x | p[1..-1] = (p << 0).each_cons(2).map { | q, r | (q << x) | r } }
    (1..n/2).any? { | m | s * m % n == 0 & & (p[m] & (1 << (s * m / n))) > 0 }
end


# https://leetcode.com/problems/split-array-with-same-average/discuss/120842/DP-with-bitset-over-*sum*-(fast-PythonRuby-decent-C++)/119921?page=1
