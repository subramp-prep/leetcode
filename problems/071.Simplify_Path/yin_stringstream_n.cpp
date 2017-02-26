class Solution {
public:
    string simplifyPath(string path)
    {
        // stack
        stack<string> stk;
        stringstream ss(path);
        
        string tmp;
        while (getline(ss,tmp,'/')) // getline (stringstream, first token, spliter)
        {
            // push to stack
            if (tmp == "" || tmp == ".") continue;
            else if (tmp == "..") { if (!stk.empty()) stk.pop();}
            else stk.push(tmp);
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