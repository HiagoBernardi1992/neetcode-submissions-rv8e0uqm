class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let countChar = new Set();
        let left = 0;
        let longestSubstring = 0;

        for (let right = 0; right < s.length; right++) {
            while (countChar.has(s[right])) {
                countChar.delete(s[left]);
                left++;
            }
            
            countChar.add(s[right]);
            
            longestSubstring = Math.max(longestSubstring, right - left + 1);
        }
        return longestSubstring;
    }
}
