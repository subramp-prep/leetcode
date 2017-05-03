// Divide and Conquer + Recursion
// Time Complexity O(2^n)
// Space Complexity O(n*2^n)
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;
        int n = input.size();
        for (int i = 0; i < n; ++i) {
            if (!isdigit(input[i])) {
                char opr = input[i];
                
                // divide to 2 parts
                vector<int> res1 = diffWaysToCompute(input.substr(0, i));
                vector<int> res2 = diffWaysToCompute(input.substr(i + 1));
                
                // combine results
                for (auto n1 : res1)
                    for (auto n2 : res2)
                        switch (opr) {
                            case '+': res.push_back(n1 + n2); break;
                            case '-': res.push_back(n1 - n2); break;
                            case '*': res.push_back(n1 * n2); break;
                        }
            }
        }
        
        // no operator exists in the string => only a number
        if (res.empty())
            res.push_back(stoi(input));
        return res;
    }
};