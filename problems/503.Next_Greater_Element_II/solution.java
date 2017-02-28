public int[] nextGreaterElements(int[] nums) {
    int n = nums.length, next[] = new int[n];
    Arrays.fill(next, -1);
    Stack<Integer> stack = new Stack<>(); // index stack
    for (int i = 0; i < n * 2; i++) {
        int num = nums[i % n];
        while (!stack.isEmpty() && nums[stack.peek()] < num)
            next[stack.pop()] = num;
        if (i < n) stack.push(i);
    }
    return next;
}
// https://discuss.leetcode.com/topic/77923/java-10-lines-and-c-12-lines-linear-time-complexity-o-n-with-explanation
// The approach is same as Next Greater Element I
// See explanation in my solution to the previous problem
// The only difference here is that we use stack to keep the indexes of the decreasing subsequence