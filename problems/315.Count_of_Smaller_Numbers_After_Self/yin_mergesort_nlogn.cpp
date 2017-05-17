// Divide & Conquer
// Time Complexity O(nlogn)
// Space Complexity O(n)
class Solution {
protected:
    void merge_countSmaller(vector<int>& ind, int l, int r, vector<int>& res, vector<int>& nums) {
        if (r - l > 1) {
            // Split
            int mid = l + (r - l) / 2;
            merge_countSmaller(ind, l, mid, res, nums);
            merge_countSmaller(ind, mid, r, res, nums);
            
            // Merge
            vector<int> tmp; // index temp array
            int i = l, j = mid;
            int semicount = 0; // number of merged elements in right subarray so far
            while ((i < mid) || (j < r)) {
                if ((j == r) || ((i < mid) && (nums[ind[i]] <= nums[ind[j]]))) { // put value of left subarray
					tmp.push_back(ind[i]);
                    res[ind[i]] += semicount; // all elements that's been merged in right subarray are smaller
                    ++i;
                } else { // put value of right subarray
					tmp.push_back(ind[j]);
                    ++semicount;
                    ++j;
                }
            }
            move(tmp.begin(), tmp.end(), ind.begin() + l); // replace indices
        }
    }
	
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        vector<int> ind(n, 0); // original index of each number
        iota(ind.begin(), ind.end(), 0); // [0..n]
        merge_countSmaller(ind, 0, n, res, nums);
        return res;
    }
};