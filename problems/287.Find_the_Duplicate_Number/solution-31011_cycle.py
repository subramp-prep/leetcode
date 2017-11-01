def findDuplicate(self, nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            return finder

# In this problem, nums[a] = b can be seen as a.next = b, the the problem
# is exactly the same as Linked List Cycle II which finds the node that
# cycle begins.
