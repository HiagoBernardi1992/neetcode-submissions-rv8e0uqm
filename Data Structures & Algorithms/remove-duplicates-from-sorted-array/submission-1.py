class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums) 

        slow = 1
        hold = nums[0]
        for fast in range(1, len(nums)):
            if hold != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
                hold = nums[fast]
        return slow

