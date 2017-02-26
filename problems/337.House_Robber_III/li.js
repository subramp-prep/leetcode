//337. House Robber III
// 向下递归，返回［plan1，plan2］数组，向上返回

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function(root) {
    var plan = rob0(root);
    console.log(root);
    return Math.max(plan[0],plan[1]);
};

var rob0 = function(root) {
    //console.log(root);
    if(root===null) return [0,0];
    if(root.right===null && root.left===null) {
        return [root.val, 0];
    }
    var tmpLeft  = rob0(root.left);
    var tmpRight  = rob0(root.right);
    return [root.val + tmpLeft[1] + tmpRight[1], Math.max(tmpLeft[0], tmpLeft[1]) + Math.max(tmpRight[0], tmpRight[1])];
};