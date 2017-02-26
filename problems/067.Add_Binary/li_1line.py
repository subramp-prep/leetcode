# 7:40-7:41
class Solution(object):

  def addBinary(self, a, b):
    return bin((int(a, 2) + int(b, 2)))[2:]

  def addBinary(self, a, b):
    return bin(eval('0b' + a) + eval('0b' + b))[2:]

  def addBinary(self, a, b):
    return bin(eval("0b%s+0b%s" % (a, b)))[2:]

  def addBinary(self, a, b):
    return bin(eval('0b' + a + '+0b' + b))[2:]

  def addBinary(self, a, b):
    return '{:b}'.format(int(a, 2) + int(b, 2))


# bin((int(a, 2) + int(b, 2)))[2:] is the best

# Why guess when it's so easy to measure? :-)
# Yes, eval is much slower, even if the string is already prefixed with '0b':

# >>> from timeit import timeit
# >>> timeit("int('1010101010101010', 2)")
# 0.82430828797186
# >>> timeit("eval('0b1010101010101010')")
# 15.573771070163502
