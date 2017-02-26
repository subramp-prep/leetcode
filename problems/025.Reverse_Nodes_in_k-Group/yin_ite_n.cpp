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
        
        // get length
        int l = 0, n;
        ListNode *ptr = head;
        while (ptr) { ptr = ptr->next; ++l; }
        
        // get nb of lists to reverse
        n = l / k;
        
        // reverse
        ListNode *res = head, *prec = NULL, *newHead = head; ptr = head->next;
        for (int i = 0; i < n; ++i)
        {
            // reverse list of k nodes
            for (int j = 1; j < k; ++j)
            {
                head->next = ptr->next;
                ptr->next = newHead;
                newHead = ptr;
                ptr = head->next;
            }
            if (i == 0) res = newHead;
            else prec->next = newHead;
            if (i < n - 1)
            {
                prec = head;
                head = newHead = ptr;
                ptr = ptr->next;
            }
        }
        
        return res;
    }
};