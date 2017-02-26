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
        // This solution works fine with small ints, but it will cause problem with int greater than MAX_INT
        // Calculate sum
        ListNode *p1 = l1, *p2 = l2;
        unsigned long long val1 = 0, val2 = 0;
        while(p1) { val1 = 10 * val1 + p1->val; p1 = p1->next;}
        while(p2) { val2 = 10 * val2 + p2->val; p2 = p2->next;}
        unsigned long long sum = val1 + val2;
        
        // Build result
        ListNode *res = NULL, *temp = NULL;
        if (!sum) { res = new ListNode(0); return res; } // case 0;
        while(sum)
        {
            int n = sum % 10;
            sum = sum / 10;
            temp = new ListNode(n);
            temp->next = res;
            res = temp;
        }
        return res;
    }
};