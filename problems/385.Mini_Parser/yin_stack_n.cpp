class Solution {
public:
    NestedInteger deserialize(string s)
    {
        stack<NestedInteger> nis;
        nis.push(NestedInteger()); // dummy head
        
        for (int i = 0; i < s.size();)
        {
            if (isNumber(s[i])) // add value ni as element
            {
                int j = i;
                while (isNumber(s[j])) ++j;
                nis.top().add(NestedInteger(stoi(s.substr(i, j - i))));
                i = j;
            }
            else
            {
                if (s[i] == '[') // push : create ni
                    nis.push(NestedInteger());
                    
                if (s[i] == ']') // pop : add list ni as element
                {
                    NestedInteger temp = nis.top();
                    nis.pop();
                    nis.top().add(temp);
                }
                ++i;
            }
        }
        
        return nis.top().getList()[0];
    }
    
    bool isNumber(char c) { return isdigit(c) || c == '-'; }
};