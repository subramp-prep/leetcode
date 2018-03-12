
    class Solution {
        public int[] kthSmallestPrimeFraction(int[] a, int K) {
            Arrays.sort(a);
            double low = 0, high = 1;
            int n = a.length;
            for(int rep = 0;rep < 50;rep++){
                double x = low + (high-low)/2;
                long num = 0;
                for(int i = 0;i < n;i++){
                    int ind = Arrays.binarySearch(a, (int)(x*a[i]));
                    if(ind < 0)ind = -ind-2;
                    num += ind+1;
                }
                if(num >= K){
                    high = x;
                }else{
                    low = x;
                }
            }

            for(double eps = 1e-14;;eps *= 10){
                for(int i = 0;i < n;i++){
                    double ln = high * a[i];
                    for(int j = 0;j < i;j++){
                        if(Math.abs(ln-a[j]) < eps){
                            return new int[]{a[j], a[i]};
                        }
                    }
                }
            }
        }
    }