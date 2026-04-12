class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let counter = new Map;
        for(let num of nums) {
            if(counter.has(num)) counter.set(num, counter.get(num) + 1);
            else counter.set(num, 1);
        }

        let result = [];        
        let values = [...counter.entries()];
        values.sort((a, b) => b[1] - a[1]);
        for (let i = 0; i < k; i++) {
            result.push(values[i][0]);
        }

        return result;
    }
}
