struct ListNode* oddEvenList(struct ListNode* head) {
     struct ListNode nodes[2] = {{0, NULL}, {0, NULL}};
     struct ListNode * lists[2] = {&nodes[0], &nodes[1]};
     for(int flag = 0; head; head = head->next, flag = !flag) lists[flag] = lists[flag]->next = head;
     lists[0]->next = nodes[1].next;
     lists[1]->next = NULL;
     return nodes[0].next;
}