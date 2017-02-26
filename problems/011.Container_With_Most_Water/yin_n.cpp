class Solution {
public:
    int maxArea(vector<int>& height)
    {
        // really similar to question 3
        
        // i : index of left line
        // j : index of right line
        int n = height.size(), water = 0, i = 0, j = n - 1;
        
        // we start with the widest container
        while (i < j)
        {
            // get height
            int h = min(height[i], height[j]);
            water = max(water, (j - i) * h);
            
            // find the next container with a larger height
            while (height[i] <= h && i < j) ++i;
            while (height[j] <= h && i < j) --j;
        }
        
        return water;
    }
};