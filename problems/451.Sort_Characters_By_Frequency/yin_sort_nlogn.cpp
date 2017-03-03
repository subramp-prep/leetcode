class Solution {
public:
    string frequencySort(string s)
    {
        // get frequencies
        vector<int> freq(128, 0);
        for (char ch : s) ++freq[ch];
            
        // custom sort
        auto cmp = [&](char a, char b) { return freq[a] > freq[b] || (freq[a] == freq[b] && a < b); };
        sort(s.begin(), s.end(), compare);
        return s;
    }
};