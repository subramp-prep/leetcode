// Priority Queue
// Time Complexity O(klogk)
// Space Complexity O(k)
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k)
    {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<pair<int, int>> res;
        if (n1 == 0 || n2 == 0 || k == 0) return res; // empty input
        
        // priority queue : stock indexes of pairs
        auto cmp = [&nums1, &nums2](pair<int, int> i1, pair<int, int> i2) // custom compare
        {
            return nums1[i1.first] + nums2[i1.second] > nums1[i2.first] + nums2[i2.second]; 
        }; 
        priority_queue<pair<int,int>, vector<pair<int, int> >, decltype(cmp)> pq(cmp);
        
        // push first possible pairs formed by nums2[0] and all values in nums1
        for (int i = 0; i < min(n1, k); ++i) pq.push(make_pair(i, 0));
            
        // get top of pq and update pq adding values in nums2
        while (!pq.empty() && k-- > 0)
        {
            pair<int, int>cur = pq.top(); pq.pop();
            res.push_back(make_pair(nums1[cur.first], nums2[cur.second]));
            if(cur.second == nums2.size() - 1) continue;
            pq.push(make_pair(cur.first, cur.second + 1));
        }
        
        return res;
    }
};