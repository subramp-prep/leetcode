class Solution
{
public:
    // In statistics, the median is used for dividing a set into two equal length subsets
	// that one subset is always greater than the other
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
		int m = nums1.size(), n = nums2.size();
		
		// let nums1 shorter than nums2
		/// to make sure i, j always have positive values
		if (m > n)
			return findMedianSortedArrays(nums2, nums1);
		
		int i, // i is where we cut nums1 => len(left_nums1) = i, len(right_nums1) = m - i
		    j, // j is where we cut nums2 => len(left_nums2) = j, len(right_nums2) = n - j
		    imin = 0, imax = m,         // 
		    half_len = (m + n + 1) / 2;
		
		// the key is to use binary search to divide nums1 and nums2 separately
	    // obtain i in [0, m] and j in [0, n] satisfying :
	    /// 1. two equal length subsets : j = (m + n + 1)/2 - i
        /// 2. the left subsets are smaller than right subsets : sums2[j-1] <= sums1[i] and sums1[i-1] <= sums2[j]
		while (imin <= imax)
		{
			i = (imin + imax) / 2;  // start binary search in [imin, imax]
			j = half_len - i;       // for equal length
			
			if (i < m && nums2[j - 1] > nums1[i])
			{
				// i is too small, must increase it
				imin = i + 1;
			}
			else if (i > 0 && nums1[i - 1] > nums2[j])
			{
				// i is too big, must decrease it
				imax = i - 1;
			}
			else
			{
			    // i is perfect : 
			    /// (j == 0 or i == m or B[j-1] <= A[i]) and
			    /// (i == 0 or j == n or A[i-1] <= B[j])
				break;
			}
		}
		
		// Get max of left subset
		int max_of_left;
		if (i == 0)         // the case that all numbers in sums1 are greater than that in nums2
			max_of_left = nums2[j - 1];
		else if (j == 0)    // the case that all numbers in sums2 are greater than that in nums1
			max_of_left = nums1[i - 1];
		else                // the case that we divide nums1 and sums2 separately
			max_of_left = max(nums1[i - 1], nums2[j - 1]);
		
		// Odd number case
		 if ((m + n) % 2 != 0)
			 return max_of_left;
		
		// Even number case
		// Get min of right subset
		int min_of_right;
		if (i == m)         // the case that all numbers in sums1 are smaller than that in nums2
			min_of_right = nums2[j];
        else if (j == n)    // the case that all numbers in sums2 are smaller than that in nums1
			min_of_right = nums1[i];
        else                // the case that we divide nums1 and sums2 separately
			min_of_right = min(nums1[i], nums2[j]);
		
        return (max_of_left + min_of_right) / 2.0;
    }
};