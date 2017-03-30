class Solution(object):

    def complexNumberMultiply(self, a, b):
        def cvt(x):
            a, b = x[:-1].split('+')
            return int(a) + int(b) * 1j
        c = cvt(a) * cvt(b)
        return "%d+%di" % (int(c.real), int(c.imag))
