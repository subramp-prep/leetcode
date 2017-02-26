//DP about 600ms
class Solution {
public:
    bool canCross(vector<int>& stones) {
        if(stones.size()<2)
            return true;
        if(stones[0]+1!=stones[1])
            return false;
        unordered_map<int, set<int>> mp;
        unordered_set<int> st;
        for(int pos:stones){
            set<int> t;
            mp[pos] = t;
            //st.insert(pos);
        }
        mp[stones[1]].insert(1);
        for (int pos:stones) {
            for (auto it =mp[pos].begin(); it!=mp[pos].end();it++) { 
                if(mp.find(pos +*it - 1)!=mp.end())
                    mp[pos+*it - 1].insert(*it-1);
                if(mp.find(pos+*it)!=mp.end())
                    mp[pos + *it].insert(*it);
                if(mp.find(pos+*it + 1)!=mp.end())
                    mp[pos +*it + 1].insert(*it + 1);
                // if(st.find(pos+ *it - 1)!=st.end())
                //     mp[pos + *it - 1].insert(*it - 1);
                // if(st.find(pos+ *it)!=st.end())
                //     mp[pos +*it].insert(*it);
                // if(st.find(pos +*it + 1)!=st.end())
                //     mp[pos + *it + 1].insert(*it + 1);
            }
        }
        
        return !mp[stones.back()].empty();
    }
};