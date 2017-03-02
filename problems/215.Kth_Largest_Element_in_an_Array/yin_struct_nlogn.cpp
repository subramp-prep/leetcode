

// Built-in priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 0; i < k - 1; i++)
            pq.pop(); // retrieve number with higher priority (larger value here)
        return pq.top();
    }
}; 

// Built-in multiset, very similar to priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
	{
        multiset<int> mset;
        int n = nums.size();
        for (int i = 0; i < n; i++)
		{ 
            mset.insert(nums[i]);
            if (mset.size() > k)
                mset.erase(mset.begin()); // erease the largest number
        }
        return *mset.begin();
    }
};