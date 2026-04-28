class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let dummy = new ListNode(0, head);
        let slow = dummy;
        let fast = head;

        // 1. Dá uma vantagem de 'n' passos para o fast
        while (n > 0 && fast) {
            fast = fast.next;
            n--;
        }

        // 2. Move ambos até o fast chegar no fim (null)
        while (fast) {
            slow = slow.next;
            fast = fast.next;
        }

        // 3. O slow agora está EXATAMENTE antes do nó que deve ser removido
        // Removemos o nó pulando ele
        slow.next = slow.next.next;

        return dummy.next;
    }
}