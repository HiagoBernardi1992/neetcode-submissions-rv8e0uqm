class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        if(k > nums.length) return undefined;
        const res = [];
        const deque = []; // Guardará ÍNDICES

        for (let i = 0; i < nums.length; i++) {
            // 1. Remova números menores do final (eles nunca serão o máximo)
            while (deque.length > 0 && nums[deque[deque.length - 1]] <= nums[i]) {
                deque.pop();
            }
            
            // 2. Adiciona o índice atual
            deque.push(i);

            // 3. Remova o índice do início se ele saiu da janela
            if (deque[0] === i - k) {
                deque.shift();
            }

            // 4. Se a janela já atingiu o tamanho k, o primeiro do deque é o max
            if (i >= k - 1) {
                res.push(nums[deque[0]]);
            }
        }
        return res;
    }
}
