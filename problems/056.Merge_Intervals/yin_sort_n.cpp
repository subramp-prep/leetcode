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
        
        // sort vector
        auto cmp = [](Interval a, Interval b) { return a.start < b.start; }; // lambda
        sort(intervals.begin(), intervals.end(), cmp);
        
        // merge
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i)
            if (res.back().end < intervals[i].start)
                res.push_back(intervals[i]);
            else
                res.back().end = max(res.back().end, intervals[i].end);
        return res;
    }
};