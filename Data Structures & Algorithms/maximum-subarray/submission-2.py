class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = 0
        sum = 0
        for n in nums:
            if n + sum > 0:
                sum = n + sum
                maximum = max(maximum, sum)
            else:
                sum = 0
        if maximum == 0:
            return max(nums)
        else:
            return maximum