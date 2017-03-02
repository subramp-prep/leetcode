def evalRPN(tokens):
    stack = []
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    for s in tokens:
        try:
            stack.append(float(s))
        except:
            stack.append(int(ops[s](stack.pop(-2), stack.pop(-1))))
    return int(stack[-1])
