def findPermutation(self, s):
  a = range(1, len(s) + 2)
  for m in re.finditer('D+', s):
    i, j = m.start(), m.end() + 1
    a[i:j] = a[i:j][::-1]
  return a


# If it's all just I, then the answer is the numbers in ascending order.
# And if there are streaks of D, then just reverse the number streak under
# each:

# My 5 - liner does exactly that. Start from sorted, then find the D -
# streaks and reverse the numbers under them:

# https://discuss.leetcode.com/topic/76276
