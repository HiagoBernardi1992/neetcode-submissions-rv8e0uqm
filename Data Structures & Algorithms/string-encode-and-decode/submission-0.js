class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = "";
        for(let str of strs)
            encoded += str.length + "#" + str;
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i = 0;

        while (i < str.length) {
            // 1. Achar onde termina o número (o próximo #)
            let j = i;
            while (str[j] !== "#") {
                j++;
            }

            // 2. O número está entre i e j
            let length = parseInt(str.substring(i, j));
            
            // 3. A palavra começa DEPOIS do # (j + 1)
            // e termina após 'length' caracteres
            let start = j + 1;
            let end = start + length;
            
            res.push(str.substring(start, end));

            // 4. Move o ponteiro i para o início da próxima contagem
            i = end;
        }

        return res;
    }
}
