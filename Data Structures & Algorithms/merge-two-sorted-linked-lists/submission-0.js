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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        // Criamos o nó "Dummy" (fictício) para ser o ponto de partida
        let dummy = new ListNode();
        // 'tail' (rabo) é quem vai percorrer e construir a lista
        let tail = dummy;

        // Enquanto as duas listas tiverem elementos
        while (list1 !== null && list2 !== null) {
            if (list1.val <= list2.val) {
                tail.next = list1; // Pendura o nó da list1
                list1 = list1.next; // Move o ponteiro da list1
            } else {
                tail.next = list2; // Pendura o nó da list2
                list2 = list2.next; // Move o ponteiro da list2
            }
            tail = tail.next; // Move o rabo da nossa nova lista para o último nó inserido
        }

        // Se uma lista acabou, "espetamos" o que sobrou da outra diretamente
        if (list1 !== null) {
            tail.next = list1;
        } else if (list2 !== null) {
            tail.next = list2;
        }

        // Retornamos dummy.next porque o dummy em si é apenas um nó vazio inicial
        return dummy.next;
    }
}
