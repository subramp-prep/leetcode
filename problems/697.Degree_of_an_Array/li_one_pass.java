import java.util.*;
class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>(), first = new HashMap<>();
        int res = 0, degree = 0;
        for (int i = 0; i < nums.length; ++i) {
            first.putIfAbsent(nums[i], i);
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);
            if (counter.get(nums[i]) > degree) {
                degree = counter.get(nums[i]);
                res = i - first.get(nums[i]) + 1;
            } else if (counter.get(nums[i]) == degree)
                res = Math.min(res, i - first.get(nums[i]) + 1);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int nums [] = new int[] {1, 2, 2, 3, 1};
        System.out.println(s.findShortestSubArray(nums));
    }
}
