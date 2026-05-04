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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        // Caso base: se os arrays estiverem vazios, não há nó
        if (preorder.length === 0 || inorder.length === 0) return null;

        // 1. O primeiro elemento do preorder é sempre a raiz
        let rootVal = preorder[0];
        let root = new TreeNode(rootVal);

        // 2. Encontramos onde a raiz está no inorder para dividir as subárvores
        let middle = inorder.indexOf(rootVal);

        // 3. Recursão para construir os filhos
        // Subárvore Esquerda:
        // Preorder: pula a raiz, pega a quantidade de elementos à esquerda (middle)
        // Inorder: pega tudo antes do middle
        root.left = this.buildTree(
            preorder.slice(1, middle + 1), 
            inorder.slice(0, middle)
        );

        // Subárvore Direita:
        // Preorder: pega tudo após os elementos da subárvore esquerda
        // Inorder: pega tudo após o middle
        root.right = this.buildTree(
            preorder.slice(middle + 1), 
            inorder.slice(middle + 1)
        );

        return root;
    }
}
