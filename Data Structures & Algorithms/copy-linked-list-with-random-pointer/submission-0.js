// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
      if (!head) return null;

        // O mapa associa NóOriginal -> NóCópia
        const oldToCopy = new Map();

        // 1ª passada: Criar todos os nós novos e guardar no mapa
        let current = head;
        while (current) {
            oldToCopy.set(current, new Node(current.val));
            current = current.next;
        }

        // 2ª passada: Conectar os ponteiros next e random
        current = head;
        while (current) {
            let copy = oldToCopy.get(current);
            // Se o próximo original for null, Map.get(null) retorna undefined, 
            // então usamos || null para garantir
            copy.next = oldToCopy.get(current.next) || null;
            copy.random = oldToCopy.get(current.random) || null;
            current = current.next;
        }

        return oldToCopy.get(head);
    }
}
