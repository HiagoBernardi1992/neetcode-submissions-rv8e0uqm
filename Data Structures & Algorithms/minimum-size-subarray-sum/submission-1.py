class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        current_sum = 0
        l = 0
        
        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum >= target:
                minimum = min(minimum, r - l + 1)
                current_sum -= nums[l]
                l += 1
                
        return minimum if minimum != float('inf') else 0
                
                