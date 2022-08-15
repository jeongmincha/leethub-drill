/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    if (!root) {
        return [];
    }
    
    const answer = [];
    const stack = [root];
    
    curr = root;
    while (stack.length > 0) {        
        if (curr && curr.left) {
            stack.push(curr.left);
            curr = curr.left;
        } else {
            curr = stack.pop();
            curr.left = null;
            if (curr) {
                answer.push(curr.val);
            }
            
            if (curr && curr.right) {
                stack.push(curr.right);
                curr = curr.right;
            }
        }
    }
    
    return answer;
};