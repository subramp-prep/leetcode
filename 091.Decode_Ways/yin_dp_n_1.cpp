class Solution {
public:
    int numDecodings(string s)
    {
        if (s.empty()) return 0;
        
        int n = s.size();
        int pprec = 1, prec = s[0] > '0', res = prec; // init

        // dp
        for (int i = 1; i < n; ++i)
        {
            res = prec * (s[i] > '0'); 
            int val = stoi(s.substr(i - 1, 2));
            res += pprec * (val >= 10 && val <= 26);
			pprec = prec;
			prec = res;
        }
        return res;
    }
};