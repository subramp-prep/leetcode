class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l1 = []
        self.l2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.l1.append(x)
        self.l2.append(min(x, self.getMin()))

    def pop(self):
        """
        :rtype: void
        """
        self.l2.pop()
        return self.l1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.l2[-1] if self.l2 else float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
