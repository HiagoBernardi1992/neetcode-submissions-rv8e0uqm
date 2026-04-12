class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const waitingResults = new Map();
    
        for (let i = 0; i < nums.length; i++) {
            if (waitingResults.has(nums[i])) {
                return [waitingResults.get(nums[i]), i];
            } 
            
            let complemento = target - nums[i];
            waitingResults.set(complemento, i);
        }
    }
}
