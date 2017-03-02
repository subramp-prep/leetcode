// 仍然有问题，要debug
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        return select(nums, 0, nums.size() - 1, k - 1);
    }
    
    // select
    int select(vector<int>& nums, int start, int end, int k)
    {
        // end condition
        if (start >= end) return nums[start];
        
        // get medians of each of [n/5] groups
        vector<int> medians;
        for (int i = start; i <= end; i += 5)
            medians.push_back(getMedian(nums, i, min(i + 4, end)));
        
        // get median of medians as pivot for partition
        int pivot = select(medians, 0, medians.size() - 1, medians.size() / 2);
        
        // partition
        int i = partition(nums, start, end, pivot);
        
        // recursion
        if (i == k)
            return nums[i]; // end condition
        else if (i < k)
            return select(nums, i + 1, end, k); // select in right part
        else if (i > k)
            return select(nums, start, i - 1, k); // select in left part
    }
    
    // get median
    int getMedian(vector<int>& nums, int i, int j)
    {
        sort(nums.begin() + i, nums.begin() + j);
        return nums[(i + j) / 2];
    }
    
    // partition
    int partition(vector<int>nums, int start, int end, int pivot)
    {
        int i = start, j = end;
        while (i < j)
        {
            while (i < j && nums[i] > pivot) ++i;
            while (i < j && nums[j] <= pivot) --j;
            swap(nums[i], nums[j]); // swap value <= pivot to right and value > pivot to left
        }
        return j;
};