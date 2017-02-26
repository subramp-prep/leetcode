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
    ListNode* swapPairs(ListNode* head)
    {
        // use dummy to avoid head check in the loop
        ListNode dummy(0), *prec = &dummy, *ptr = head;
        dummy.next = head;
        while (ptr && ptr->next)
        {
            ListNode *temp = ptr->next->next;
            ptr->next->next = ptr;
            prec->next = ptr->next;
            prec = ptr;
            ptr = ptr->next = temp;
        }
        return dummy.next;
    }
};