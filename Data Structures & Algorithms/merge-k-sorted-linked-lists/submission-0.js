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
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        if (!lists || lists.length === 0) return null;

        while (lists.length > 1) {
            let tempMergedList = [];

            for (let i = 0; i < lists.length; i += 2) {
                let l1 = lists[i];
                let l2 = (i + 1 < lists.length) ? lists[i + 1] : null;
                
                tempMergedList.push(this.mergeList(l1, l2));
            }
            lists = tempMergedList;
        }

        return lists[0];
    }

    mergeList(listOne, listTwo) {
        let dummy = new ListNode();
        let tail = dummy;

        while(listOne !== null && listTwo !== null) {
            if(listOne.val <= listTwo.val) {
                tail.next = listOne;
                listOne = listOne.next;
            } else {
                tail.next = listTwo;
                listTwo = listTwo.next;
            }
            tail = tail.next;
        }

        if(listOne != null) {
            tail.next = listOne;
        } else {
            tail.next = listTwo;
        }

        return dummy.next;
    }
}
