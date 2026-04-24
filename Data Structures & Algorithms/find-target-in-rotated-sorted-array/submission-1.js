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

            if(nums[start] <= nums[middle]) {
                if(target >= nums[start] && target < nums[middle])
                    end = middle - 1;
                else
                    start = middle + 1;
            } else {
                if(target > nums[middle] && target <= nums[end])
                    start = middle + 1;
                else
                    end = middle - 1;
            }
        }
        return -1;
    }
}
