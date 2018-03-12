    class Solution {
        public int findCheapestPrice(int n, int[][] es, int src, int dst, int K) {
            long[] ds = new long[n];
            Arrays.fill(ds, Long.MAX_VALUE / 2);
            ds[src] = 0;
            long ans = ds[dst];
            for(int i = 0;i < K+1;i++){
                long[] nds = new long[n];
                Arrays.fill(nds, Long.MAX_VALUE / 2);
                for(int[] e : es){
                    nds[e[1]] = Math.min(nds[e[1]], ds[e[0]] + e[2]);
                }
                ds = nds;
                ans = Math.min(ans, ds[dst]);
            }
            return ans < Integer.MAX_VALUE ? (int)ans : -1;
        }
    }