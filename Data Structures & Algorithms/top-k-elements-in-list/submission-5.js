class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let counter = new Map();
        let bucket = Array.from({ length: nums.length + 1 }, () => []);

        for (let num of nums) {
            counter.set(num, (counter.get(num) || 0) + 1);
        }

        for (let [num, freq] of counter) {
            bucket[freq].push(num);
        }

        let result = [];
        for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
            if (bucket[i].length > 0) {
                result.push(...bucket[i]);
            }
        }

        return result.slice(0, k);
    }
}
