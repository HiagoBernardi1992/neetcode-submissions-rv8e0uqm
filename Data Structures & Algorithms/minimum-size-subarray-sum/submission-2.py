class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minimum = min(minimum, r - l +1)
                sum -= nums[l]
                l += 1

        return minimum if minimum != float('inf') else 0
                 
        
                
                