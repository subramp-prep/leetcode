import itertools
import time


nums = range(15)
left = "%-30s"
print left % "AC but not list: combinations",
start = time.time()
[l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
print time.time() - start

print left % "AC: list combinations",
start = time.time()
[list(l) for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
print time.time() - start


print left % "RF: filter none and 0, product",
start = time.time()
[filter(None, l) for l in itertools.product(*zip(nums, [None] * len(nums)))]
print time.time() - start

print left % "AC: filter none, product",
start = time.time()
[filter(lambda x: x != None, l) for l in itertools.product(*zip(nums, [None] * len(nums)))]
print time.time() - start


print left % "AC: generator, product",
start = time.time()
[[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]
print time.time() - start

print left % "AC: reduce",
start = time.time()
reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])
print time.time() - start


print left % "AC: bits",
start = time.time()
[[nums[i] for i in range(len(nums)) if mask >> i & 1]
 for mask in range(2 ** len(nums))]
print time.time() - start


print left % "AC: fast bits",
start = time.time()


def subsets(nums):
    n = len(nums)
    subsets = [[]] * 2**n
    for i in xrange(n):
        subsets[1 << i] = [nums[i]]
    for mask in xrange(1, 2**n):
        subsets[mask] = subsets[mask & -mask] + subsets[mask & mask - 1]
    return subsets
subsets(nums)
print time.time() - start
