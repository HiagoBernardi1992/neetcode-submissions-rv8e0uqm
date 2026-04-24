class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let res = nums[0];
        let start = 0;
        let end = nums.length - 1;
        while(start <= end) {
            if(nums[start] < nums[end]) {
                res = Math.min(res, nums[start]);
                break;
            } 
            let middle = Math.floor(start + (end - start) / 2);
            res = Math.min(res, nums[middle]);
            if(nums[middle] >= nums[start]) start = middle + 1;
            else end = middle - 1;
        }
        return res;
    }
}
