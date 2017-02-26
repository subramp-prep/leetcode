# 7:40-7:41
class Solution(object):

  def addBinary(self, a, b, c=0, res=''):
    if len(a) or len(b) or c:
      if len(a):
        c += int(a[-1])
        a = a[:-1]
      if len(b):
        c += int(b[-1])
        b = b[:-1]
      return self.addBinary(a, b, c // 2, str(c % 2) + res)
    return res

s = Solution()
print s.addBinary('0', '0')
print s.addBinary('100', '110010')
