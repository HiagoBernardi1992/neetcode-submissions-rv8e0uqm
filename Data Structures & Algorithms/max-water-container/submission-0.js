class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let start = 0;
        let end = heights.length - 1;
        let maxWaterHeight = 0;
        while(start < end) {
            let width = end - start;
            let heigth = Math.min(heights[start], heights[end]);
            let currentHeight = width * heigth;
            maxWaterHeight = Math.max(maxWaterHeight, currentHeight);
            if(heights[start] < heights[end]) start++;
            else end--;
        }
        return maxWaterHeight;
    }
}
