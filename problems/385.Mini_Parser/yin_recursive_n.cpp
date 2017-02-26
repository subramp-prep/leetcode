class Solution {
public:
    NestedInteger deserialize(string s)
    {
        // end condition
        if (s.empty()) return NestedInteger(); // empty string
        if (s[0] != '[') return NestedInteger(stoi(s)); // number string
        
        // res
        NestedInteger res;
        for (int i = 1; i < s.size();)
        {
            // value ni OR list ni
			if (isNumber(s[i]) || s[i] == '[')
			{
				int j = i; // end of substring for recursion
				
				if (isNumber(s[i])) // value ni
					while (isNumber(s[j])) ++j; // end of number string
				
				if (s[i] == '[') // list ni
				{
					int cnt = 1;
					while (cnt > 0) { ++j; cnt = s[j] == '[' ? cnt + 1 : s[j] == ']' ? cnt - 1 : cnt; } // pos of correspondent ']'
				}
				
				res.add(deserialize(s.substr(i, j - i)));
				i = j;
			}
			else
                ++i;
        }
        return res;
    }
    
    bool isNumber(char c) { return isdigit(c) || c == '-'; }
};