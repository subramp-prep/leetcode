def isUgly(self, num):
    return num > 0 == 30**32 % num

# Don't worry about the runtime, it's mostly judge overhead. Check this out:


def isUgly(self, num):
    return [num > 0 == 30**32 % num for _ in range(1000)][-1]

# That does it 1000 times and gets accepted in about 420 ms.
# Meaning the actual solution takes only about 0.4 ms and the rest of the
# ~60 ms is judge overhead, and it varies considerably.

# https://discuss.leetcode.com/topic/42589/python-1-line-solution
