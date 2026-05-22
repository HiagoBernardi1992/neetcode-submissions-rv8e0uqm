class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let counter = new Map;
        for(var i = 0; i < nums.length; i++) {
            if(counter.has(nums[i])) counter.set(nums[i], +1);
            else counter.set(nums[i], 1);
        }        
        let j = 0;
        let response = [];
        console.log(counter);
        while(j < k) {
            let maxKey = [...counter.keys()].reduce((a, b) =>
                counter.get(a) > counter.get(b) ? a : b
            );
            response.push(maxKey);
            counter.delete(maxKey);
            j++;
        } 
        return response;
    }
}
