def judgePoint24(self, nums):
    from operator import truediv, mul, add, sub
    from fractions import Fraction

    def apply(A, B):
        ans = set()
        for x, y, op in itertools.product(A, B, (truediv, mul, add, sub)):
            if op is not truediv or y: ans.add(op(x, y))
            if op is not truediv or x: ans.add(op(y, x))
        return ans

    A = [{x} for x in map(Fraction, nums)]
    for i, j in itertools.combinations(range(4), 2):
        r1 = apply(A[i], A[j])
        k, l = {0, 1, 2, 3} - {i, j}
        if 24 in apply(apply(r1, A[k]), A[l]): return True
        if 24 in apply(apply(r1, A[l]), A[k]): return True
        if 24 in apply(r1, apply(A[k], A[l])): return True

    return False

# We write a function apply that takes two sets of possibilities for A and
# B and returns all possible results operator(A, B) or operator(B, A) for
# all possible operators.

# Ignoring reflection, there are only two ways we can apply the operators:
# (AB)(CD) or ((AB)C)D. When C and D are ordered, this becomes three ways
# - the third way is ((AB)D)C.

# This solution is a little slow because it has to manage sets - my
# article has a solution that is almost 10x faster. I think this one is
# cool though.
