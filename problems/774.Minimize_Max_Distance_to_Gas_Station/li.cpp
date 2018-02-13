class Solution {
public:
    double minmaxGasDist(vector<int>& st, int K) {
        int count, N = st.size();
        double left = 0, right = st[N - 1] - st[0], mid;
        while (left + 1e-6 < right) {
            mid = (left + right) / 2;
            count = 0;
            for (int i = 0; i < N - 1; ++i)
                count += ceil((st[i + 1] - st[i]) / mid) - 1;
            if (count > K) left = mid;
            else right = mid;
        }
        return right;
    }
};i