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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode *res = NULL, *curr = NULL;
        int carry = 0;
        
        while (l1 != NULL || l2 != NULL)
        {
            int p = (l1) ? l1->val : 0;
            int q = (l2) ? l2->val : 0;
            int sum = p + q + carry;
            carry = sum / 10;
            sum = sum % 10;
            
            if (res == NULL)
            {
                res = new ListNode(sum);
                curr = res;
            }
            else
            {
                curr->next = new ListNode(sum);
                curr = curr->next;
            }
            
            l1 = (l1) ? l1->next : NULL;
            l2 = (l2) ? l2->next : NULL;
        }
        
        if (carry > 0)
            curr->next = new ListNode(carry);
        
        return res;
    }
};