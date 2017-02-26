def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left - 1, right)
        if right > left:
            generate(p + ')', left, right - 1)
        if not right:
            parens += p,
        return parens
    return generate('', n, n)

# p is the parenthesis-string built so far,
# left and right tell the number of left and right parentheses still to add,
# and parens collects the parentheses.

# I used a few "tricks"... how many can you find? :-)
