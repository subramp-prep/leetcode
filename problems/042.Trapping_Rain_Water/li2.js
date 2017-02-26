/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
	var count = [],
		left = 0,
		right = height.length - 1,
		ret = 0;
		seaLevel = 0;
	while (left + 1 < right) {
		if (height[left] <= seaLevel) {
			left++;
			if (seaLevel > height[left]) {
				ret += seaLevel - height[left];
			}
		} else if (height[right] <= seaLevel) {
			right--;
			if (seaLevel > height[right]) {
				ret += seaLevel - height[right];
			}
		} else {
			seaLevel = Math.min(height[left],height[right]);
		}
	}
	return ret;
};

var height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
console.log(trap(height));