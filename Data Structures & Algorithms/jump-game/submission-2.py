class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # jumps = nums[0]
        # for i in range(1, len(nums)):
        #     if jumps <= 0:
        #         return False
        #     jumps -= 1
        #     jumps = max(jumps, nums[i])
        # return True
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

        

