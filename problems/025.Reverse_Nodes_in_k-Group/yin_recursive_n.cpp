/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k)
    {
        if (!head || !head->next || k <= 1) return head;
        
        // Check validity of k
        ListNode *next = head;
        for (int i = 0; i < k; ++i) { if (!next) return head; next = next->next; }
        
        // reverse
        ListNode *prec = NULL, *ptr = head;
        while (ptr != next)
        {
            ListNode *temp = ptr->next;
            if (prec)
                ptr->next = prec;
            else
                ptr->next = reverseKGroup(next, k);
            prec = ptr;
            ptr = temp;
            
        }
        return prec;
    }
};