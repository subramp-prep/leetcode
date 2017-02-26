class Solution {
public:
    // The only rule to respect is : for a pair of parentheses, add '(' before ')'
    vector<string> generateParenthesis(int n)
    {
        vector<string> res;
        addPar(res, "", n, 0);
        return res;
    }
    
    void addPar(vector<string> &v, string str, int nLeft, int nRight)
    {
		// end condition
        if(nLeft == 0 && nRight == 0) { v.push_back(str); return; }
		
		// add parenthese
        if(nLeft > 0){ addPar(v, str + "(", nLeft - 1, nRight + 1); }
        if(nRight > 0){ addPar(v, str + ")", nLeft, nRight - 1); }
    }
};