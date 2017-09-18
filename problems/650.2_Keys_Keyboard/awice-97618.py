# We can break the total sequence of operations into groups that take the form "[copy][some number of pastes]" In K operations of this group, the length of the string is multiplied by K.

# Now, suppose N can be written as N = d_1 * d_2 * ... * d_k.

# By the above reasoning, N "A"s can be written on the tape in d_1 + d_2 + ... + d_k operations. If any of the d_i are composite, say d_i = p*q (with p>1, q>1), then we could write it in p + q instead of p*q operations by breaking up this divisor.

# For example, if we make 15 with 15 operations, we could instead make it with 3 operations to get AAA then another 5 operations. Also, we should justify that p+q <= p*q (because (p-1)(q-1) is positive), so we indeed do get savings by breaking up this product.

def minSteps(self, n):
    def factors(n):
        d = 2
        while d * d <= n:
            while n % d == 0:
                n /= d
                yield d
            d += 1
        if n > 1:
            yield n

    return sum(factors(n))