class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length) return false;
        let countOfLetter = {};
        for(let i = 0; i < s.length; i++) {
            if(countOfLetter[s[i]]) {
                countOfLetter[s[i]]++;
            } else {
                countOfLetter[s[i]] = 1;
            }
        }

        for(let i = 0; i < t.length; i++) {
            if(countOfLetter[t[i]]) {
                countOfLetter[t[i]]--;
            } else {
                return false;
            }
        }

        return Object.values(countOfLetter).some(counter => counter != 0) ? false : true;
    }
}
