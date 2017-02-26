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
    ListNode* removeNthFromEnd(ListNode* head, int n)
    {
        ListNode *p1 = head, *p2 = head;
        
        // create an offset pointer p2
        for (int i = 0; i < n; ++i)
            p2 = p2->next;
        
        // if it's head
        if (p2 == NULL)
        {
            p1 = head->next;
            delete head;
            return p1;
        }
            
        
        // iterate p1 according to p2
        while(p2->next != NULL)
        {
            p2 = p2->next;
            p1 = p1->next;
        }
        p2 = p1->next;
        p1->next = p2->next;
        delete p2;
        return head;
        
    }
};