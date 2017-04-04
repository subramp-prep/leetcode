// Sort
// Time Complexity O(n)
// Space Complexity O(n)
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals)
    {
        vector<Interval> res;
        // corner case
        if (intervals.empty()) return res;
        
        // sort starts and ends
        int n = intervals.size();
        vector<int> starts;
        vector<int> ends;
        for (int i = 0; i < n; ++i)
        {
            starts.push_back(intervals[i].start);
            ends.push_back(intervals[i].end);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        
        // form intervals
        for (int i = 0, j = 0; i < n; ++i)
            if (i == n - 1 || starts[i + 1] > ends[i])
            {
                res.push_back(Interval(starts[j], ends[i]));
                j = i + 1;
            }
        return res;
    }
};