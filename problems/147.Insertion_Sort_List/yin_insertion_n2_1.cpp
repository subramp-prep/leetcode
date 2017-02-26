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
    ListNode* insertionSortList(ListNode* head)
    {
        if (!head || !head->next) return head;
        ListNode *ptri, *ptrj = head->next, *preci, *precj = head, *insert = NULL;
        while (ptrj)
        {
            preci = NULL;
            ptri = head;
            while(ptri != ptrj)
            {
                if (ptri->val > ptrj->val)
                {
                    // remove node to insert
                    precj->next = ptrj->next;
                    ptrj->next = NULL;
                    insert = ptrj;
                    ptrj = precj;
                    
                    // insert
                    if (preci == NULL)
                    {   
                        insert->next = head;
                        head = insert;
                    }
                    else
                    {
                        insert->next = ptri;
                        preci->next = insert;
                    }
                    break;
                }
                preci = ptri;
                ptri = ptri->next;
            }
            precj = ptrj;
            ptrj = ptrj->next;
        }
        return head;
    }
};