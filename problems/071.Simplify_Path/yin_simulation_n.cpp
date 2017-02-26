class Solution {
public:
    string simplifyPath(string path)
    {
        // stack
        stack<string> stk;
        
        int i = 0;
        while (i < path.size())
        {
            if (path[i] == '/')
            {
                // get path descp
                int j = ++i;
                while (path[j] != '/' && j < path.size()) ++j;
                string tmp = path.substr(i, j - i);
                i = j;
                
                // push to stack
                if (tmp == "" || tmp == ".") continue;
                else if (tmp == "..") { if (!stk.empty()) stk.pop();}
                else stk.push(tmp);
            }
        }
        
        // build result
        string res = "";
        while (!stk.empty())
        {
            res = "/" + stk.top() + res;
            stk.pop();
        }
        return res.empty() ? "/" : res;
    }
};