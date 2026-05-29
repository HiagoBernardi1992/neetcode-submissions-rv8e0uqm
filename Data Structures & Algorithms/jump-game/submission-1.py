class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        for i in range(1, len(nums)):
            if jumps <= 0:
                return False
            jumps -= 1
            jumps = max(jumps, nums[i])
        return True
