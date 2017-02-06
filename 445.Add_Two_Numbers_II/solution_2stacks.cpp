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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> f1, f2;
        ListNode *res = new ListNode(0);
        int sum  = 0;
        while(l1){f1.push(l1->val);l1 = l1->next;}
        while(l2){f2.push(l2->val);l2 = l2->next;}

        while(!f1.empty() || !f2.empty()){
            if(!f1.empty()){sum+=f1.top();f1.pop();}
            if(!f2.empty()){sum+=f2.top();f2.pop();}
            res->val = sum % 10;
            ListNode* head = new ListNode(sum /= 10);
            head->next = res;
            res = head;
        }
        return res->val? res : res->next;
    }
};

//https://discuss.leetcode.com/topic/65279
//https://discuss.leetcode.com/topic/65279/easy-o-n-java-solution-using-stack/7