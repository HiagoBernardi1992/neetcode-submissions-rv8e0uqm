class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        if(strs.length <= 1) {
            return [strs];
        }
        let answer = {};
        for(let str of strs) {
            const count = new Array(26).fill(0);
            for (let char of str) {
                const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
                count[index]++;
            }
            const key = count.join('#');
            if(answer[key]) answer[key].push(str);
            else answer[key] = [str];
        }
        return Object.values(answer);
    }
}
