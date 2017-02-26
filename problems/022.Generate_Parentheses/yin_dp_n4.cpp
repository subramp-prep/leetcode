class Solution {
public:
    // we can generate parentheses step by step
    vector<string> generateParenthesis(int n)
    {
        // an array to stock all precedent steps
        vector<vector<string>> steps;
        
        // Init : step 0
        vector<string> step0(1, "");
        steps.push_back(step0);
        
        // generate
        for (int i = 1; i <= n; ++i) // step i
        {
            vector<string> stepi;
            for (int j = 0; j < i; ++j)
                for (int k = 0; k < steps[j].size(); ++k)
                    for (int h = 0; h < steps[i - j - 1].size(); ++h)
                        stepi.push_back(steps[j][k]+"("+steps[i - j - 1][h]+")");
            steps.push_back(stepi);
        }
        return steps[n];
    }
};