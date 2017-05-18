// Divide and Conquer + Merge Sort
// Time Complexity O(nlogn)
// Space Complexity O(n)
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        if (n <= 0) return 0;
        
        // Build sum array
        vector<long long>sums(1, nums[0]);
        for (int i = 1; i < n; ++i)
            sums.push_back(sums[i - 1] + nums[i]);
        
        // Merge sort
        return merge_countRangeSum(sums, 0, n - 1, lower, upper);
    }
    
    int merge_countRangeSum(vector<long long>& sums, int l, int r, int lower, int upper) {
        // End condition
        if (r == l) return (lower <= sums[l]) && (sums[r] <= upper);
        
        // Divide
        int mid = l + (r - l) / 2;
        int res = merge_countRangeSum(sums, l, mid, lower, upper)
                    + merge_countRangeSum(sums, mid + 1, r, lower, upper);
        
        // Conquer: [l, mid] and [mid + 1, r] are sorted, count crossing ranges
        int m = mid + 1, n = mid + 1;
        for (int i = l, j = 0; i <= mid; ++i, ++j) {
            while (m <= r && sums[m] - sums[i] < lower) ++m;
            while (n <= r && sums[n] - sums[i] <= upper) ++n;
            res += n - m;
        }
        
        // Merge
        inplace_merge(sums.begin() + l, sums.begin() + mid + 1, sums.begin() + r + 1);
        
        return res;
    }
};