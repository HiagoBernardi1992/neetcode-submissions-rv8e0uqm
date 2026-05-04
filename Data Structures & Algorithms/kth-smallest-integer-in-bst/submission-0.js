/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let n = 0;
        let stack = [];
        let curr = root;
        while(curr || stack.length > 0) {
            while(curr) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            n++;
            if(n == k) return curr.val;
            else curr = curr.right;
        }
        return stack
    }
}
