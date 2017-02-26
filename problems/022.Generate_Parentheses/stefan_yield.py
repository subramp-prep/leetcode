def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left - 1, right):
                yield q
            for q in generate(p + ')', left, right - 1):
                yield q
    return list(generate('', n, n))


# Here I wrote an actual Python generator.
# I allow myself to put the yield q at the end of the line
# because it's not that bad and because in "real life"
# I use Python 3 where I just say yield from generate(...).
