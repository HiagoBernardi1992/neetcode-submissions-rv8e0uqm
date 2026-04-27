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
     * @return {void}
     */
    reorderList(head) {
        if (!head || !head.next) return;

        // 1. Encontrar o meio
        let slow = head;
        let fast = head.next;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 2. Inverter a segunda metade
        let second = slow.next;
        slow.next = null; // Corta a lista em duas
        let prev = null;
        
        while (second) {
            let tmp = second.next; // Salva o PRÓXIMO real
            second.next = prev;    // Inverte a seta
            prev = second;         // Move o prev
            second = tmp;          // Move o second para o próximo original
        }

        // 3. Intercalar as duas metades (Merge)
        // 
        let first = head;
        second = prev; // 'prev' é o head da lista invertida
        while (second) {
            let tmp1 = first.next;
            let tmp2 = second.next;

            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2;
        }
    }
}
