class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let startIndex = 0;
        let endIndex = nums.length - 1;

        while (startIndex <= endIndex) {
            let middleIndex = this.calcMiddleIndex(startIndex, endIndex);

            if (nums[middleIndex] === target) {
                return middleIndex;
            }

            if (nums[middleIndex] > target) {
                endIndex = middleIndex - 1;
            } else {
                startIndex = middleIndex + 1;
            }
        }

        return -1;
    }

    calcMiddleIndex(start, end) {
        return Math.floor(start + (end - start) / 2);
    }
}
