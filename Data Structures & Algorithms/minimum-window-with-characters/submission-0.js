class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if(t.length > s.length) return "";

        let countT = new Map();
        for(let char of t)
            countT.set(char, (countT.get(char) || 0) + 1);

        let countS = new Map();
        let need = countT.size; // Quantos caracteres únicos precisamos satisfazer
        let have = 0;
        let res = [-1, -1];
        let minLen = Infinity;
        let startI = 0;

        for (let i = 0; i < s.length; i++) {
            let char = s[i];
            countS.set(char, (countS.get(char) || 0) + 1);

            // Se atingimos a quantidade necessária desse caractere específico
            if (countT.has(char) && countS.get(char) === countT.get(char)) {
                have++;
            }

            // Enquanto a janela for válida, tentamos encolher
            while (have === need) {
                // 1. Atualiza o menor resultado encontrado
                if ((i - startI + 1) < minLen) {
                    minLen = i - startI + 1;
                    res = [startI, i];
                }

                // 2. Tira o caractere da esquerda
                let leftChar = s[startI];
                countS.set(leftChar, countS.get(leftChar) - 1);
                
                // 3. Se ao tirar, a janela deixou de ser válida, diminui o 'have'
                if (countT.has(leftChar) && countS.get(leftChar) < countT.get(leftChar)) {
                    have--;
                }
                
                startI++; // Move a cauda da janela
            }
        }

        return minLen === Infinity ? "" : s.substring(res[0], res[1] + 1);
    }
}
