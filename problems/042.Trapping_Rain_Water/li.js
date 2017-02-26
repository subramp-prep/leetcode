/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
	var count = [];
	count[0] = height[0];
	for (var i = 1; i < height.length; i++) {
		count[i] = Math.max(count[i - 1], height[i]);
	}
	var count2 = [];
	count2[height.length - 1] = height[height.length - 1];
	for (var i = height.length - 2; i >= 0; i--) {
		count2[i] = Math.max(count2[i + 1], height[i]);
	}
	var ret = 0;
	for (var i = 0; i < height.length; i++) {
		ret += Math.min(count[i] , count2[i]) - height[i];
	}
	return ret;
};

var height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
console.log(trap(height));