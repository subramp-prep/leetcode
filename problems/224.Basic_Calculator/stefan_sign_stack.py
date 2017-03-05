def calculate(self, s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        # print '%11s   %-16s %2d' % (s[i:], signs, total)
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'],
        elif c == ')':
            signs.pop()
        i += 1
    return total

# https://discuss.leetcode.com/topic/15806/easy-18-lines-c-16-lines-python
