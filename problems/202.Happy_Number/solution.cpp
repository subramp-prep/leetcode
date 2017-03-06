class Solution {
public:
    int happy(int n) {
        int next = 0;
        while (n) {
            next += (n % 10) * (n % 10);
            n /= 10;
        }
        return next;
    }

    bool isHappy(int n) {
        int slow, fast;
        slow = fast = n;
        do {
            slow = happy(slow);
            fast = happy(fast);
            fast = happy(fast);
        } while(slow != fast);
        if (slow == 1) return 1;
        else return 0;
    }
};

//https://discuss.leetcode.com/topic/12587/my-solution-in-c-o-1-space-and-no-magic-math-property-involved
//I see the majority of those posts use hashset to record values. Actually, 
// we can simply adapt the Floyd Cycle detection algorithm. 
// I believe that many people have seen this in the Linked List Cycle detection problem. 

