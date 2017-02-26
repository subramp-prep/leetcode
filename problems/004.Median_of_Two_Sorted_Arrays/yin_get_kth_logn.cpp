class Solution {
public:
    // this question can be seen as "Find the (m+n+1)/2 th biggest number in two sorted arrays"
    // or "Find the (m+n+1)/2 th and ((m+n)/2)+1 biggest numbers in two sorted arrays"
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        int m = nums1.size(), n = nums2.size();
        
        if ( (m + n) % 2 == 0)
        {
            int k1 = (m + n + 1) / 2;
            int k2 = (m + n) / 2 + 1;
            return (getkth(nums1, nums2, k1) + getkth(nums1, nums2, k2)) / 2.0;
        }
        else
        {
            int k = (m + n + 1) / 2;
            return getkth(nums1, nums2, k);
        }
    }
    
    // create a recursive function to get the kth value from two arrays
    // similar to recursion in binary search
    int getkth(vector<int>& v1, vector<int>& v2, int k)
    {
        // get sizes
        int m = v1.size(), n = v2.size();
        
        // let v1 shorter than v2
        if (m > n) 
            return getkth(v2, v1, k);
        
        // end condition  
        if (m == 0)
            return v2[k - 1];
        if (k == 1)
            return min(v1[0], v2[0]);
        
        // recursion
        /// compare the k/2 th numbers in v1 and v2
		/// because there must be k-1 numbers smaller than the kth number and one array must have more of them
		/// by comparing their k/2 th number, we can figure out which array it is
        int i = min(m, k / 2), j = min(n, k / 2);
		/// the array that has a smaller k/2 th number has more numbers smaller than the kth number
		/// and we won't find the kth number in its first k/2 numbers => remove them
		if (v1[i - 1] > v2[j - 1])
        {
            vector<int> newV2(v2.begin() + j, v2.end());
            return getkth(v1, newV2, k - j);
        }
        else
        {
            vector<int> newV1(v1.begin() + i, v1.end());
            return getkth(newV1, v2, k - i);
        }
        return 0;
    }
};