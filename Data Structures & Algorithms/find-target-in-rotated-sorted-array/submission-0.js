class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let start = 0;
        let end = nums.length - 1;
        while(start <= end) {
            let middle = Math.floor(start + (end - start) / 2);
            if(nums[middle] === target) return middle;

            if((nums[middle] > nums[end] && target <= nums[end]) 
            || (nums[middle] < nums[end] && nums[middle] < target))
                start = middle + 1;
            else 
                end = middle - 1;
        }
        return -1;
    }
}
