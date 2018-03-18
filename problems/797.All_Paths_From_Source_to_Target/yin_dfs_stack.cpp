// Depth First Search
// Time Complexity O(2^n)
// Space Complexity O(n*2^n)
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        // Corner case
        if (graph.size() == 0)
			return res;
		
		stack<vector<int>> stk;
		// Init stack path 0->1
		for (int n : graph[0]) {
			stk.push({0, n});
		}
		
		while (!stk.empty()) {
			vector<int> path = stk.top(); stk.pop();
            if (path.back() == graph.size() - 1) {
                res.push_back(path); // complete path
            } else {
                for (int n : graph[path.back()]) {
                    vector<int> stk_path = path;
                    stk_path.push_back(n);
                    stk.push(stk_path); // incomplete path
                }
            }
		}
		return res;
    }
};