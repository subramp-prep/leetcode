class Solution(object):

    def numComponents(self, head, G):
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                    getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next

        return ans
