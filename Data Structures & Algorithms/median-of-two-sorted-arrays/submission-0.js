class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let A = nums1;
    let B = nums2;
    const total = A.length + B.length;
    const half = Math.floor((total + 1) / 2);

    // Garantir que A seja o menor array para otimizar a busca
    if (B.length < A.length) {
        [A, B] = [B, A];
    }

    let l = 0;
    let r = A.length;

    while (l <= r) {
        let i = Math.floor((l + r) / 2); // Partição em A
        let j = half - i;               // Partição em B

        // Pegamos os valores das bordas (com Infinity para casos vazios)
        let A_left = i > 0 ? A[i - 1] : -Infinity;
        let A_right = i < A.length ? A[i] : Infinity;
        let B_left = j > 0 ? B[j - 1] : -Infinity;
        let B_right = j < B.length ? B[j] : Infinity;

        // Verificamos se a partição está correta
        if (A_left <= B_right && B_left <= A_right) {
            // Se o total for ímpar, a mediana é o maior dos esquerdos
            if (total % 2 !== 0) {
                return Math.max(A_left, B_left);
            }
            // Se for par, é a média entre os dois do meio
            return (Math.max(A_left, B_left) + Math.min(A_right, B_right)) / 2;
        } 
        else if (A_left > B_right) {
            // A parte esquerda de A está muito grande, movemos a faca para a esquerda
            r = i - 1;
        } else {
            // A parte esquerda de A está muito pequena, movemos para a direita
            l = i + 1;
        }
    }
    }
}
