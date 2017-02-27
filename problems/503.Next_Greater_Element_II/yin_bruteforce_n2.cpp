// Flag
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> res(n, -1);
        
        for (int i = 0; i < n; ++i)
        {
            bool flag = false;
            // search from i + 1 to the end
            for (int j = i + 1; j < n; ++j)
                if (nums[j] > nums[i]) { flag = true; res[i] = nums[j]; break;}
                
            // search from 0 to i - 1
            if (!flag)
                for (int j = 0; j < i; ++j)
                    if (nums[j] > nums[i]) { res[i] = nums[j]; break;}
        }
        return res;
    }
};

// Mod
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> res(n, -1);
        
        for (int i = 0; i < n; ++i)
        {
            for (int j = (i + 1) % n; j != i; j = (j + 1) % n)
            {
                if (nums[i] < nums[j])
                {
                    res[i] = nums[j];
                    break;
                }
            }
        }
        return res;
    }
};