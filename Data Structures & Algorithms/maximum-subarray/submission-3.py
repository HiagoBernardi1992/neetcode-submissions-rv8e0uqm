class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0

            sum = sum + n
            maximum = max(maximum, sum)

        return maximum
