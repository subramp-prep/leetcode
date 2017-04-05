class Solution:
    # @param num, a list of integers
    # @return a string

    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(num).lstrip('0') or '0'

    def largestNumber2(self, num):
        return ''.join(sorted(itertools.imap(str, num), cmp=lambda x, y: cmp(y + x, x + y))).lstrip('0') or '0'
