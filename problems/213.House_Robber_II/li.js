//213 House Robber II
//转化为 198 House Robber I

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length===0) return 0;
    if(nums.length===1) return nums[0];
    if(nums.length==2) return Math.max(nums[0],nums[1]);
    if(nums.length==3) return Math.max(nums[0],nums[1],nums[2]);
    var line1 = nums.slice(1);
    var line2 = nums.slice(2);
    line2.push(nums[0]);
    return Math.max(rob1(line1), rob1(line2));
};

var rob1 = function(nums) {
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