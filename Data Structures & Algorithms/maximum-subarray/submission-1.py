class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maximum = 0
        sum = 0
        for n in nums:
            if n + sum > 0:
                sum = n + sum
                maximum = max(maximum, sum)
            else:
                sum = 0
        return maximum