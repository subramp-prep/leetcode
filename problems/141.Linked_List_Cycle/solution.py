def hasCycle(self, head):
    fast = slow = head
    while slow and fast and fast.next:
        slow = slow.next                # Step of 1
        fast = fast.next.next           # Setp of 2
        if slow is fast:                # Checking whether two pointers meet
            return True
    return False
