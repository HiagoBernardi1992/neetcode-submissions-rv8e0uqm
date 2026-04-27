/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        let data = new Set();
        let current = head;
        while(current) {
            if(data.has(current)) return true;
            else {
                data.add(current);
                current = current.next;
            }
        }
        return false;
    }
}
