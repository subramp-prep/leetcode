# In Python I was only able to do it with a rather ugly wrapper:
def firstBadVersion(self, n):
    class Wrap:

        def __getitem__(self, i):
            return isBadVersion(i)
    return bisect.bisect(Wrap(), False, 0, n)

# Nicer, more readable version:


def firstBadVersion(self, n):
    return bisect.bisect(type('', (), {'__getitem__': lambda self, i: isBadVersion(i)})(), False, 0, n)
