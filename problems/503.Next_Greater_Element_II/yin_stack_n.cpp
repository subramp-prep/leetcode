// Loop once using mod
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> stk;
        
        for (int i = 0; i < n * 2; ++i)
        {
            int num = nums[i % n]; 
            while (!stk.empty() && nums[stk.top()] < num) // look back to find smaller value
            {
                res[stk.top()] = num;
                stk.pop();
            }
            if (i < n) stk.push(i); // push index of current num to be filled
            if (stk.empty()) break; // all indexes filled
        }
        return res;
    }
};

// Loop twice
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums)
    {
        // init
        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> stk;
        
        for (int i = 0; i < n; ++i)
        {
            int num = nums[i];
            while (!stk.empty() && nums[stk.top()] < num) // look back to find smaller values
            {
                res[stk.top()] = num;
                stk.pop();
            }
            stk.push(i); // push index of current num to be filled
        }
        
        for (int i = 0; i < n; ++i)
        {
            int num = nums[i];
            while (!stk.empty() && nums[stk.top()] < num) // look back to find smaller values
            {
                res[stk.top()] = num;
                stk.pop();
            }
            if (stk.empty()) break; // all indexes filled
        }
        return res;
    }
};