class Solution {
public:

    //  Method returns true if nums can be partitioned into K subsets
    // with equal sum
    bool canPartitionKSubsets(vector<int>& nums, int K)
    {
        int N = nums.size();
        //  If K is 1, then complete array will be our answer
        if (K == 1) return true;

        //  If total number of partitions are more than N, then
        // division is not possible
        if (N < K) return false;

        // if array sum is not divisible by K then we can't divide
        // array into K partitions
        int sum = 0;
        for (int i = 0; i < N; i++) sum += nums[i];
        if (sum % K != 0) return false;

        //  the sum of each subset should be subset (= sum / K)
        int subset = sum / K;
        int subsetSum[K];
        bool taken[N];

        //  Initialize sum of each subset from 0
        for (int i = 0; i < K; i++) subsetSum[i] = 0;

        //  mark all elements as not taken
        for (int i = 0; i < N; i++) taken[i] = false;

        // initialize first subsubset sum as last element of
        // array and mark that as taken
        subsetSum[0] = nums[N - 1];
        taken[N - 1] = true;

        //  call recursive method to check K-substitution condition
        return canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, 0, N - 1);
    }

    // Recursive Utility method to check K equal sum
    // subsetition of array
    /**
        array           - given input array
        subsetSum array   - sum to store each subset of the array
        taken           - boolean array to check whether element
                          is taken into sum partition or not
        K               - number of partitions needed
        N               - total number of element in array
        curIdx          - current subsetSum index
        limitIdx        - lastIdx from where array element should be taken
    */
    bool canPartitionKSubsets(vector<int>& nums, int subsetSum[], bool taken[], int subset, int K, int N, int curIdx, int limitIdx) {
        if (subsetSum[curIdx] == subset) {
            /*  current index (K - 2) represents (K - 1) subsets of equal
                sum last partition will already remain with sum 'subset'*/
            if (curIdx == K - 2) return true;

            //  recursive call for next subsetition
            return canPartitionKSubsets(nums, subsetSum, taken, subset,
                                        K, N, curIdx + 1, N - 1);
        }

        //  start from limitIdx and include elements into current partition
        for (int i = limitIdx; i >= 0; i--) {
            //  if already taken, continue
            if (taken[i]) continue;
            int tmp = subsetSum[curIdx] + nums[i];

            // if temp is less than subset then only include the element
            // and call recursively
            if (tmp <= subset) {
                //  mark the element and include into current partition sum
                taken[i] = true;
                subsetSum[curIdx] += nums[i];
                bool nxt = canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, curIdx, i - 1);
                // after recursive call unmark the element and remove from
                // subsetition sum
                taken[i] = false;
                subsetSum[curIdx] -= nums[i];
                if (nxt) return true;
            }
        }
        return false;
    }

};