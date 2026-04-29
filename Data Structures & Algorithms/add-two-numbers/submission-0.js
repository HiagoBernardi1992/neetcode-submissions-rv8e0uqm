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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
      let dummy = new ListNode();
      let currDummy = dummy;
      let curr1 = l1;
      let curr2 = l2;
      let carry = 0;
      while(curr1 || curr2 || carry != 0) {
        let v1 = curr1 ? curr1.val : 0;
        let v2 = curr2 ? curr2.val : 0;
        let sum = this.getSum(v1, v2, carry);
        let val = this.getVal(sum);
        carry = this.getCarry(sum);
        let newNode = new ListNode(val);
        if (curr1) curr1 = curr1.next;
        if (curr2) curr2 = curr2.next;
        currDummy.next = newNode;
        currDummy = currDummy.next;
      }
      return dummy.next;
    }

    getCarry(sum) {
      return Math.floor(sum / 10);
    }

    getVal(sum) {
      return sum % 10;
    }

    getSum(val1, val2, carry) {
      return val1 + val2 + carry;
    }
}
