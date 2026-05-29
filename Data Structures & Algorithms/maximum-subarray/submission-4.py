class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        maximum = nums[0]

        for n in nums:
            current = max(n, current + n)
            maximum = max(maximum, current)

        return maximum
