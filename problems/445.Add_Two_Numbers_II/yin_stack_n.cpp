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
        // Convert to stack
        ListNode *p1 = l1, *p2 = l2, *res = NULL, *temp = NULL;
        stack<int> s1, s2;
        while(p1) { s1.push(p1->val); p1 = p1->next; }
        while(p2) { s2.push(p2->val); p2 = p2->next; }
        
        // Calculte sum
        int carry = 0, n, val1, val2;
        while (!s1.empty() || !s2.empty() || carry)
        {
            val1 = s1.empty() ? 0 : s1.top();
            val2 = s2.empty() ? 0 : s2.top();
            if (!s1.empty()) s1.pop();
            if (!s2.empty()) s2.pop();
            n = val1 + val2 + carry;
            carry = n / 10;
            n = n % 10;
            temp = new ListNode(n);
            temp->next = res;
            res = temp;
        }
        
        return res;
    }
};