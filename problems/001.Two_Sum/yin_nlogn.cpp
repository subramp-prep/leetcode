class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> hash;
        vector<int> res;
        
        // use it
        for (int i = 0; i < nums.size(); ++i)
        {
            int other = target - nums[i];
            
            if (hash.find(other) != hash.end())
            {
                res.push_back(hash[other]);
                res.push_back(i);
                return res;   
            }
            
			// add number here to make sure that it only checks the numbers before it
            hash[nums[i]] = i;
        }
    }
};