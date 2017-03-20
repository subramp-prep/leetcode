class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        // group sorted strings
        map<string, vector<int>> rec;
        for (int i = 0; i < strs.size(); ++i)
        {
            string tmp = strs[i];
            sort(tmp.begin(), tmp.end());
            rec[tmp].push_back(i);
        }
        
        // build result
        vector<vector<string>> res;
        for (map<string, vector<int>>::iterator it = rec.begin(); it != rec.end(); it++)
        {
            vector<string> grp;
            for (int j = 0; j < it->second.size(); ++j)
                grp.push_back(strs[it->second[j]]);
            res.push_back(grp);
        }
        return res;
    }
};