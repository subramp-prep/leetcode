def convertTo7(self, num):
  res = ''
  n = abs(num)
  while n:
    res = str(n % 7) + res
    n /= 7
  return '-' * (num < 0) + res or "0"
