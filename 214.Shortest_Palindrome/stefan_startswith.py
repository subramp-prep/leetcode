def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s

# What's so speical about startswith? It's implemented in C.
# Python is slow compared with C, so use startswith to avoid the Python while loop.
