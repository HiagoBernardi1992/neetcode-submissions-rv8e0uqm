class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            temp = i
            i = i + nums[i]
            if i == temp:
                return False

        return True