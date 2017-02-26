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
    ListNode* sortList(ListNode* head)
    {
        // end condition 
        if (head == NULL || head->next == NULL) return head;
        
        // split list in the middle
        ListNode *slow = head, *fast = head->next;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *head2 = slow->next;
        slow->next = NULL;
        
        // sort left and right part
        head = sortList(head); 
        head2 = sortList(head2);
        return merge(head, head2);
    }
    
    ListNode* merge(ListNode* l1, ListNode* l2)
    {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* res;
        if (l1->val <= l2->val)
        {
            l1->next = merge(l1->next, l2);
            return l1;
        }
        else
        {
            l2->next = merge(l1, l2->next);
            return l2;
        }
        return res;   
    }
};