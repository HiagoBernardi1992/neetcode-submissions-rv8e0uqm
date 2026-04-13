class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const res = new Array(n).fill(1);

        // 1ª Passada: Prefixos (Esquerda para Direita)
        // Vamos acumulando o produto de tudo o que está à ESQUERDA de i
        let prefix = 1;
        for (let i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        // 2ª Passada: Sufixos (Direita para Esquerda)
        // Vamos multiplicando o que já temos pelo produto de tudo o que está à DIREITA de i
        let suffix = 1;
        for (let i = n - 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
}
