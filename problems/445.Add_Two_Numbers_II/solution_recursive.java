/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int size1 = getLength(l1);
        int size2 = getLength(l2);
        ListNode head = new ListNode(1);
        // Make sure l1.length >= l2.length
        head.next = size1 < size2 ? helper(l2, l1, size2 - size1) : helper(l1, l2, size1 - size2);
        // Handle the first digit
        if (head.next.val > 9) {
            head.next.val = head.next.val % 10;
            return head;
        }
        return head.next;
    }
    // get length of the list
    public int getLength(ListNode l) {
        int count = 0;
        while(l != null) {
            l = l.next;
            count++;
        }
        return count;
    }
    // offset is the difference of length between l1 and l2
    public static ListNode helper(ListNode l1, ListNode l2, int offset) {
        ListNode head = l1;
        if(l1 == null) {
            return null;
        } else {
            // check whether l1 becomes the same length as l2
            l1.val = (offset == 0) ? (l1.val + l2.val) : l1.val;
            l1.next = (offset == 0) ? helper(l1.next, l2.next, 0) : helper(l1.next, l2, offset - 1);
            // handle carry 
            if (l1.next != null && l1.next.val > 9) {
                l1.next.val -= 10;
                l1.val += 1;
            }
            return head;
        }
    }
}

//https://discuss.leetcode.com/topic/65306