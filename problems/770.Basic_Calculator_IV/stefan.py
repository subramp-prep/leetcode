def basicCalculatorIV(self, expression, evalvars, evalints):
    class C(collections.Counter):

        def __add__(self, other):
            self.update(other)
            return self

        def __sub__(self, other):
            self.subtract(other)
            return self

        def __mul__(self, other):
            product = C()
            for x in self:
                for y in other:
                    xy = tuple(sorted(x + y))
                    product[xy] += self[x] * other[y]
            return product
    vals = dict(zip(evalvars, evalints))

    def f(s):
        s = str(vals.get(s, s))
        return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
    c = eval(re.sub('(\w+)', r'f("\1")', expression))
    return ['*'.join((str(c[x]),) + x)
            for x in sorted(c, key=lambda x: (-len(x), x))
            if c[x]]

# I let eval and collections.Counter do most of the work. First I wrap
# every variable and number in the given expression in a call to f. For
# example the expression e + 8 - a + 5 becomes f("e") + f("8") - f("a") +
# f("5"). Then when I eval that, my function f converts its argument to a
# C object, which is a subclass of Counter.

# A term like 42*a*a*b is represented by C({('a', 'a', 'b'): 42}). That
# is, the key is the variables as sorted tuple, and the value is the
# coefficient. So f converts free variables to C({('x',): 1}) (where x is
# the variable name) and converts known variables or numbers to C({(): x})
# (where x is the number).

# Counters already know how to add and subtract each other, but I had to
# teach them multiplication. And in the end I need to turn the resulting C
# object into the desired output format.
