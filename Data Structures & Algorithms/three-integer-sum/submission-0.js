class Solution {
    threeSum(nums) {
        // 1. Ordenar é essencial (aqui garantimos que nums é array)
        nums.sort((a, b) => a - b);
        let res = [];

        for (let i = 0; i < nums.length; i++) {
            // Pula duplicatas do primeiro elemento (fixo)
            if (i > 0 && nums[i] === nums[i - 1]) continue;

            let start = i + 1;
            let end = nums.length - 1;

            while (start < end) {
                let sum = nums[i] + nums[start] + nums[end];

                if (sum === 0) {
                    res.push([nums[i], nums[start], nums[end]]);                    
                    start++;
                    end--;

                    while (start < end && nums[start] === nums[start - 1]) {
                        start++;
                    }
                } else if (sum > 0) {
                    end--;
                } else {
                    start++;
                }
            }
        }
        return res;
    }
}