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
        if (!head || !head->next) return head;
        quickSort(head, NULL);
        return head;
    }
    
    void quickSort(ListNode* start, ListNode* end)
    {
        // end condition
        if (start == end) return;
        
        // get pivot index
        ListNode* p = partition(start, end);
        
        // recursive
        quickSort(start, p);
        quickSort(p->next, end);
    }
    
    ListNode* partition(ListNode* start, ListNode* end)
    {
        ListNode *res = start, *ptr = res->next;
        while (ptr != end)
        {
            if (ptr->val < start->val)
            {
                res = res->next;
                swap(ptr, res);
            }
            ptr = ptr->next;
        }
        swap(res, start);
        return res;
    }
    
    void swap(ListNode* n1, ListNode* n2)
    {
        int temp = n1->val;
        n1->val = n2->val;
        n2->val = temp;
    }
};