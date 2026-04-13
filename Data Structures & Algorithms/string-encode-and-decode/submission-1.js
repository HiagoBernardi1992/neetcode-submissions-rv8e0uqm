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

        while(i < str.length) {
            // 1. find the next #
            let j = i;
            while(str[j] != "#") j++;

            //the length is between i and j
            let length = parseInt(str.substring(i, j));

            let start = j + 1;
            let end = start + length;
            res.push(str.substring(start, end));

            i = end;
        }

        return res;
    }
}
