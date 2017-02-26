public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    //求l1，l2长度
    int n1 = 0, n2 = 0;
    for (ListNode i = l1; i != null; i = i.next) n1++;
    for (ListNode i = l2; i != null; i = i.next) n2++;
    // 相加推入stack
    Stack<Integer> st = new Stack();
    int totn = Math.max(n1, n2);
    for (ListNode i = l1, j = l2; totn > 0; totn--) {
        int a = 0, b = 0;
        if (totn <= n1) { a = i.val; i = i.next;}
        if (totn <= n2) { b = j.val; j = j.next;}
        st.push(a + b);
    }
    //构造结果
    int c = 0;
    ListNode ans = null;
    while (!st.empty()) {
        ListNode i = new ListNode(st.pop());
        int c1 = (c + i.val) / 10;
        i.val = (c + i.val) % 10;
        i.next = ans;
        ans = i;
        c = c1;
    }
    //处理第一位
    if (c > 0) {
        ListNode i = new ListNode(c);
        i.next = ans;
        ans = i;
    }    
    return ans;
}

//https://discuss.leetcode.com/topic/65279/easy-o-n-java-solution-using-stack/5