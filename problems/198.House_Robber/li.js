//198. House Robber
// plan1, plan2 向前推进，类比斐波纳切数列。

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length===0) return 0;
    if(nums.length===1) return nums[0];
    if(nums.length==2) return Math.max(nums[0],nums[1]);
    var tmp1 = nums[0];
    var tmp2 = Math.max(nums[0],nums[1]);
    for(var i=2; i<nums.length; i++) {
        tmp = Math.max(tmp1+nums[i],tmp2);
        tmp1 = tmp2;
        tmp2 = tmp;
    }
    return tmp2;
};