class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);
        let maxFreq = 0;
        for (let num of numSet) {
            if (!numSet.has(num - 1)) {
                let count = 1;
                let currentNum = num;
                while(numSet.has(currentNum + 1)){
                    currentNum = currentNum + 1;
                    count++;
                }
                maxFreq = Math.max(maxFreq, count);
            }
        }
        return maxFreq;
    }
}
