class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let count = new Map();
        let left = 0; // Começa no zero!
        let mostFreqChar = 0;
        let maxLength = 0;

        for (let right = 0; right < s.length; right++) {
            // 1. Atualiza a contagem do caractere que entrou (right)
            let char = s[right];
            count.set(char, (count.get(char) || 0) + 1);
            
            // 2. Atualiza qual a maior frequência que já vimos na janela atual
            mostFreqChar = Math.max(mostFreqChar, count.get(char));

            // 3. A janela é válida? Se (tamanho - freq) > k, ela é INVÁLIDA
            while ((right - left + 1) - mostFreqChar > k) {
                // Remove o caractere da esquerda da contagem
                count.set(s[left], count.get(s[left]) - 1);
                // Encolhe a janela
                left++;
            }

            // 4. Se chegou aqui, a janela é válida. Medimos o tamanho máximo.
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}
