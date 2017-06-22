def deleteDuplicates(self, h):
    h and (h.next=self.delete_duplicates(h.next)) and h.next if h.next.val == h.val else h
