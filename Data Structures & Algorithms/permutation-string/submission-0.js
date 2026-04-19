class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if(s1.length > s2.length) return false;
        let countS1 = Array(26).fill(0);  
        for(let s of s1){
            const index = s.charCodeAt(0) - 'a'.charCodeAt(0);
            countS1[index]++;
        }
        let countS2 = Array(26).fill(0);
        let start = 0;
        let end = s1.length - 1;
        for(let i = 0; i < s2.length; i++) {
            const index = s2[i].charCodeAt(0) - 'a'.charCodeAt(0);
            countS2[index]++;
            if(i === end) {
                //time to compare
                if(this.areEqual(countS1, countS2)) return true;
                else {
                    const index = s2[start].charCodeAt(0) - 'a'.charCodeAt(0);
                    countS2[index]--;
                    start++;
                    end++;
                }
            }
        }

        return false;
    }

    areEqual(arr1, arr2) {
        for (let i = 0; i < 26; i++) {
            if (arr1[i] !== arr2[i]) return false;
        }
        return true;
    }
}
