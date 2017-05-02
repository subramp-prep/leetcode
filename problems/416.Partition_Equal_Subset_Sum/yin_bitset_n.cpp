// Bitset
// Time Complexity O(n)
// Space Complexity O(sum(nums)) < O(const)~O(1)
class Solution {
public:
    const static int MAX_NUM = 100;
    const static int MAX_ARRAY_SIZE = 200;
    bool canPartition(vector<int>& nums) {
        bitset<MAX_NUM * MAX_ARRAY_SIZE / 2 + 1> bits(1);
        int sum = 0;
        for (auto n : nums) {
            sum += n; // Calculate sum
            bits |= bits << n;
        }
        return !(sum & 1) // not odd number
				&& bits[sum / 2]; // sum/2 th bit not zero
    }
};