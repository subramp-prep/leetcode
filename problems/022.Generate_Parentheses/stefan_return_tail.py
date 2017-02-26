def generateParenthesis(self, n, open=0):
    if n == 0:
        return [')' * open]
    if open == 0:
        return ['(' + x for x in self.generateParenthesis(n - 1, 1)]
    else:
        return [')' + x for x in self.generateParenthesis(n, open - 1)] + ['(' + x for x in self.generateParenthesis(n - 1, open + 1)]


def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + \
               [')' + p for p in self.generateParenthesis(n, open - 1)]
    return [')' * open] * (not n)


# Solution 3

# Improved version of this.
# Parameter open tells the number of "already opened" parentheses,
# and I continue the recursion as long as
# I still have to open parentheses (n > 0)
# and I haven't made a mistake yet (open >= 0).
