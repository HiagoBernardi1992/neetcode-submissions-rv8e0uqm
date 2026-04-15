class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let start = 0;
        let end = s.length - 1;
        while (start < end) {
            // Enquanto o caractere da esquerda não for letra/número, pula
            while (start < end && !this.isAlphanumeric(s[start])) {
                start++;
            }
            // Enquanto o caractere da direita não for letra/número, pula
            while (start < end && !this.isAlphanumeric(s[end])) {
                end--;
            }

            // Agora compara (lembre-se do case-insensitive!)
            if (s[start].toLowerCase() !== s[end].toLowerCase()) {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }

    isAlphanumeric(char) {
        return /[a-z0-9]/i.test(char);
    }
}
