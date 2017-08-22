class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


# Python has more than 32 bits for integers. You can try to run "print 2
# ** 31"and Python would shows the exact number correctly, while other
# languages like Java would not. Java only recognizes - 2 ** 31 to 2 ** 31
# - 1.

# How does integers presented in Python differ from integers in 32 - bit e.g. Java?
# From what I heard, Python has 64 bits. (Please let me know if I am wrong.)
# So 1 in Python would look like 0x0000000000000001, but it looks like 0x00000001 in 32 - bit format.
# -1 in Python would look like 0xFFFFFFFFFFFFFFFF, but it looks like 0xFFFFFFFF in 32 - bit format.

# It seems that the input given by LC is in 32 - bit format. Since Python
# would treat it as positive with 1 on the 32 position, we have to use
# mask to treat it as negative.
