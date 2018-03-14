class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> res = new ArrayList<>();
        if (graph == null) {
            return res;
        }
        helper(res, new ArrayList<>(), graph, 0, graph.length - 1);
        return res;
    }

    public void helper(List<List<Integer>> res, List<Integer> path, int[][] graph, int node, int dest) {
        if (node == dest) {
            path.add(node);
            res.add(new ArrayList<>(path));
            path.remove(path.size() - 1);
            return;
        }
        for (int next : graph[node]) {
            path.add(node);
            helper(res, path, graph, next, dest);
            path.remove(path.size() - 1);
        }
    }
}