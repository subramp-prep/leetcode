class Solution {
        public boolean isBipartite(int[][] g) {
            int n = g.length;
            int[] color = new int[n];
            for(int i = 0;i < n;i++){
                if(color[i] == 0){
                    color[i] = 1;
                    if(!dfs(i, color, g))return false;
                }
            }
            return true;
        }
        boolean dfs(int cur, int[] color, int[][] g)
        {
            for(int e : g[cur]){
                if(color[e] == 0){
                    color[e] = -color[cur];
                    if(!dfs(e, color, g))return false;
                }else if(color[e] == color[cur]){
                    return false;
                }
            }
            return true;
        }
    }