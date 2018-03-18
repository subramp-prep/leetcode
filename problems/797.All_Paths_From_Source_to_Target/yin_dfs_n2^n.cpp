// Depth First Search
// Time Complexity O(2^n)
// Space Complexity O(n*2^n)
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        vector<int> path;
        getPathsSourceTarget(graph, res, path, 0, graph.size() - 1);
        return res;
    }
    
    void getPathsSourceTarget(vector<vector<int>>& graph, vector<vector<int>>& res, vector<int> path, int src, int dst) {
        path.push_back(src);
        if (src == dst) {
            res.push_back(path);
        } else {
            for (int n : graph[src]) {
                getPathsSourceTarget(graph, res, path, n, graph.size() - 1);
            }
        }
    }
};

// Time complexity is the number of all possible paths from the start point in a directed acyclic graph <= 2^n (go though an edge or not)