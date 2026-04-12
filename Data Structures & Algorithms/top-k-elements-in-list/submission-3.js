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
        let i = 0;
        let response = [];
        console.log(counter);
        while(i < k) {
            let maxKey = [...counter.keys()].reduce((a, b) =>
                counter.get(a) > counter.get(b) ? a : b
            );
            response.push(maxKey);
            counter.delete(maxKey);
            i++;
        } 
        return response;
    }
}
