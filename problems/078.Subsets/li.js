/**
 * 题目考虑顺序元素顺序。
 * 注意concat可以拷贝数组，返回新数组。元素如果是数组，拷贝的是ref。
 * 所以有copyDeep()这样的函数
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if(nums.length === 0) return [[]];
    var nums2 = nums.concat();
    var last = nums2.pop();
    var subset = subsets(nums2);
    var result = [];
    for (var i = 0; i < subset.length; ++i) {
        result.push(subset[i].concat());
    }
    for (var i = 0; i < subset.length; ++i) {
        result.push(subset[i].concat(last));
    }
    return result;
};