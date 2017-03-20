public int FindMin(int[] nums) {
    int left = 0, right = nums.Length - 1, mid = 0;
    while(left < right){
        mid = (left + right) >> 1;
        if(nums[mid] > nums[right]) left = mid + 1;
        else right = mid;
    }
    return nums[right];
}