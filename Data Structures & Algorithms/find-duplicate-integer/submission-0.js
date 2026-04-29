class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
      let count = new Set();
      for(let num of nums) {
        if(count.has(num)) return num;
        else count.add(num);
      }
    }
}
