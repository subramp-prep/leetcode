public class Solution {

    class UnionFind {

        int[] parent;
        int[] rank;
        int count;

        UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            count = n;  // number of components
            for (int i=0; i<n; ++i) { parent[i] = i; }  // initially, each node's parent is itself.
        }

        int find(int x) {
            if (x != parent[x]) {
                parent[x] = find(parent[x]);  // find root with path compression
            }
            return parent[x];
        }

        boolean union(int x, int y) {
            int X = find(x), Y = find(y);
            if (X == Y) { return false; }
            if (rank[X] > rank[Y]) { parent[Y] = X; }  // tree Y is lower
            else if (rank[X] < rank[Y]) { parent[X] = Y; }  // tree X is lower
            else {  // same height
                parent[Y] = X;
                ++rank[X];
            }
            --count;
            return true;
        }
    }

    public boolean validTree(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        for (int[] edge: edges) {
            int x = edge[0], y = edge[1];
            if (!uf.union(x, y)) { return false; }  // loop detected
        }
        return uf.count == 1;
    }
}