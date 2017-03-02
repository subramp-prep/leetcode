class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        return quickSelect(nums, 0, nums.size() - 1, k - 1);
    }
    
    // quick select
    int quickSelect (vector<int> &nums, int start, int end, int k)
    {
        // partition
        int i = start, j = end, pivot = nums[end];
        while (i < j)
        {
            while (i < j && nums[i] > pivot) ++i;
            while (i < j && nums[j] <= pivot) --j;
            swap(nums[i], nums[j]); // swap value <= pivot to right and value > pivot to left
        }
        swap(nums[j], nums[end]); // swap pivot to j
        
		// recursion
        if (j == k)
            return nums[j]; // end condition
        else if (j < k)
            return quickSelect(nums, j + 1, end, k); // select in right part
        else
            return quickSelect(nums, start, j - 1, k); // select in left part
    }
};