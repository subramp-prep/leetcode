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
    ListNode* rotateRight(ListNode* head, int k)
    {
        if (!head || !head->next || !k) return head;
        ListNode *ptr = head;
        
        // get length and make a circle
        int l = 1;
        while (ptr->next) { ptr = ptr->next; ++l;}
        ptr = ptr->next = head;
        
        // break the circle
        int cnt = l - k % l;
        while (--cnt) {ptr = ptr->next;}
        head = ptr->next;
        ptr->next = NULL;
        return head;
    }
};