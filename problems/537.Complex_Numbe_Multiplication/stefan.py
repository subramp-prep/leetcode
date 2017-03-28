# We can leverage that Python already has complex numbers and can eval expressions.


def complexNumberMultiply(self, a, b):
    z = eval(('(%s)*(%s)' % (a, b)).replace('i', 'j'))
    return '%d+%di' % (z.real, z.imag)

# Oh well, turns out it's not much work to calculate it myself:


def complexNumberMultiply(self, a, b):
    a, ai, b, bi = map(int, re.findall('-?\d+', a + b))
    return '%d+%di' % (a * b - ai * bi, a * bi + ai * b)
