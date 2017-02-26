class Solution {
public:
    int findPeakElement(vector<int>& nums)
    {
        int n = nums.size(), start = 0, end = n - 1, mid;
        while (start <= end)
        {
            mid = (start + end) / 2;
            if (mid == end) return (mid + 1 < n && nums[mid] < nums[mid + 1]) ? mid + 1 : mid;
            
            if (nums[mid] < nums[mid + 1])
                start = mid + 1;
            if (nums[mid] > nums[mid + 1])
                end = mid - 1;
        }
        return mid;
    }
};