def canMeasureWater(self, x, y, z):
    from fractions import gcd
    return z == 0 or x + y >= z and z % gcd(x, y) == 0
