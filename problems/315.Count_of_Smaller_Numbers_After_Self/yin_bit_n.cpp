// Bit Manipulation
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
private: 
    void bit_divide(vector<int>& nums, vector<int> ind, int mask, vector<int>& res) {
         if (mask == 0 || ind.size() <= 1) return;
         vector<int> lowGroup, highGroup;
         
        int high = mask < 0 ? 0 : mask;
        for (int i = 0; i < ind.size(); ++i) {
            if ((nums[ind[i]] & mask) == high) {
                res[ind[i]] += lowGroup.size();
                highGroup.push_back(ind[i]);
            } else {
                lowGroup.push_back(ind[i]);
            }
        }
         
         bit_divide(nums, lowGroup, (unsigned int)mask >> 1, res);
         bit_divide(nums, highGroup, (unsigned int)mask >> 1, res);
     }
     
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        vector<int> ind(n, 0);
        for (int i = 0; i < n; ++i) ind[i] = n - 1 - i; // [n..0]
        
        bit_divide(nums, ind, 1 << 31, res);
        return res;
    }
};