def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    return max(sorted(filter(isSubsequence, d)) + [''], key=len)


# More efficient version(no sorting):
def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    return min(filter(isSubsequence, d) + [''], key=lambda x: (-len(x), x))


# Different style:
def findLongestWord(self, s, d):
    best = ''
    for x in d:
        if (-len(x), x) < (-len(best), best):
            it = iter(s)
            if all(c in it for c in x):
                best = x
    return best

# https://discuss.leetcode.com/topic/80887/short-python-solutions

# Some comments:
# The built-in function iter() takes an iterable object and returns an iterator.
# with state that remembers where it is during iteration,
# c in it returns True if the value in the iteration and updates the state to point at the next value
# return False when it goes to the end of iteration
# just for those who are not familiar with iter() at first like me.
