def judgePoint24(self, nums):
    if len(nums) == 1:
        return math.isclose(nums[0], 24)
    return any(self.judgePoint24([x] + [num for k, num in enumerate(nums) if k not in (i, j)])
               for i, a in enumerate(nums) for j, b in enumerate(nums) if i != j
               for x in {a + b, a * b, a - b, b - a, b and a / b, a and b / a})


# Just go through all pairs of numbers a and b and replace them with a +
# b, a * b, etc. Use recursion for the now smaller list. Positive base
# case is the list being[24](or close enough).

# I prevent division - by - zero by using b and a / b instead of just a /
# b. If b is zero, then b and a / b is zero. And it's ok to have that
# zero, since a*b is zero as well. It's not even a second zero, because
# I'm creating a set of the up to six operation results, so duplicates are
# ignored immediately.

# Oh and note that I'm using Python 3, so / is "true" division, not
# integer division like in Python 2. And it would be better to use
# fractions.Fraction instead of floats. I actually just realized that
# there is in fact an input where simple floats fail, namely [3, 3, 8, 8].
# Floats calculate 23.999999999999989341858963598497211933135986328125
# instead of 24. It's not in the judge's test suite, but it should be
# soon. Using Fraction however made my solution exceed the time limit, so
# I settled for the above approximation solution.
