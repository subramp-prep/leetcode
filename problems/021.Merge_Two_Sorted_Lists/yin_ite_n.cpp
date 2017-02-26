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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
    {
        ListNode *p1 = l1, *p2 = l2, *res =  NULL, *ptr = NULL;
        int n;
        while (p1 || p2)
        {
            // get value
            if (p1 && (!p2 || p1->val <= p2->val))
            {
                n = p1->val;
                p1 = p1->next;
            }
            else
            {
                n = p2->val;
                p2 = p2->next;
            }
            
            // add value
            if (res == NULL)
            {
                res = new ListNode(n);
                ptr = res;
            }
            else
            {
                ptr->next = new ListNode(n);
                ptr = ptr->next;
            }
        }
        return res;
    }
};