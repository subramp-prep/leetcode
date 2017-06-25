6-10 lines in C++ | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  16306 

<h2>Update 4:<br/>
"Code golf" (6 lines)</h2>
<p>Not fully golfed, but yeah...</p>
<pre><code>ListNode* reverseBetween(ListNode *head, int m, int n) {
    ListNode **a = &amp;head, **b;
    for (;m--; n--)
        a = &amp;(*(b=a))-&gt;next;
    for (;n--; swap(*b, *a))
        swap(*b, (*a)-&gt;next);
    return head;
}
</code></pre>
<hr/>
<h2>Update 3:<br/>
Pointer pointers (8 lines)</h2>
<p>Removed duplicate code.</p>
<pre><code>ListNode* reverseBetween(ListNode *head, int m, int n) {
    ListNode **pivot = &amp;head, **prev;
    for (int i=0; i&lt;m; i++)
        pivot = &amp;(*(prev=pivot))-&gt;next;
    for (int i=m; i&lt;n; i++) {
        swap(*prev, (*pivot)-&gt;next);
        swap(*prev, *pivot);
    }
    return head;
}
</code></pre>
<hr/>
<h2>Update 2:<br/>
Pointer pointers (9 lines)</h2>
<p>Using a second pointer pointer.</p>
<pre><code>ListNode* reverseBetween(ListNode *head, int m, int n) {
    ListNode **prev = &amp;head;
    for (int i=1; i&lt;m; i++)
        prev = &amp;(*prev)-&gt;next;
    ListNode **pivot = &amp;(*prev)-&gt;next;
    for (int i=m; i&lt;n; i++) {
        swap(*prev, (*pivot)-&gt;next);
        swap(*prev, *pivot);
    }
    return head;
}
</code></pre>
<hr/>
<h2>Update 1:<br/>
Pointer pointer (9 lines)</h2>
<p>Motivated by quick glance at <a href="https://leetcode.com/discuss/74361/less-than-10-lines-c-double-pointer-easy-understanding" rel="nofollow">lchen77's solution</a>.</p>
<pre><code>ListNode* reverseBetween(ListNode *head, int m, int n) {
    ListNode **prev = &amp;head;
    for (int i=1; i&lt;m; i++)
        prev = &amp;(*prev)-&gt;next;
    ListNode *pivot = *prev;
    for (int i=m; i&lt;n; i++) {
        swap(*prev, pivot-&gt;next-&gt;next);
        swap(*prev, pivot-&gt;next);
    }
    return head;
}
</code></pre>
<hr/>
<h2>Dummy node (10 lines)</h2>
<p>My original one.</p>
<pre><code>ListNode* reverseBetween(ListNode *head, int m, int n) {
    ListNode dummy(0), *prev = &amp;dummy;
    dummy.next = head;
    for (int i=1; i&lt;m; i++)
        prev = prev-&gt;next;
    ListNode *pivot = prev-&gt;next;
    for (int i=m; i&lt;n; i++) {
        swap(prev-&gt;next, pivot-&gt;next-&gt;next);
        swap(prev-&gt;next, pivot-&gt;next);
    }
    return dummy.next;
}</code></pre> 

Ref: https://discuss.leetcode.com/topic/45392
