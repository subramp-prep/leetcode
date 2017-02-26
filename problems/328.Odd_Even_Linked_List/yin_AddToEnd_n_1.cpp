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
    ListNode* oddEvenList(ListNode* head)
    {
        if (!head || !head->next || !head->next->next) return head;
        ListNode *ptr = head, *loop_end = NULL, *end = head;
        while (end->next && end->next->next) end = end->next->next;
        while (ptr->next != loop_end)
        {
            ListNode *even = ptr->next;
            if (!loop_end) loop_end = even;
            ptr = ptr->next = even->next;
            even->next = end->next;
            end = end->next = even;
        }
        return  head;
    }
};