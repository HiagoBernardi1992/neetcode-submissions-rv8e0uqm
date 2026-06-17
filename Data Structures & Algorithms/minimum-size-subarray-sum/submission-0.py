class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        count = 0
        sum = 0
        l = 0
        for r in range(len(nums)):
            count += 1
            sum += nums[r]
            while sum >= target:
                minimum = min(minimum, count)
                sum -= nums[l]
                l += 1
                count -= 1

        return minimum if minimum != float('inf') else 0
                
                