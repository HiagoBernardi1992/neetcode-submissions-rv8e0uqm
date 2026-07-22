class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums[0]

        def howMuch(start, end):
            option_one = 0
            option_two = 0
            for i in range(start, end + 1):
                temp = max(option_one + nums[i], option_two)
                option_one = option_two
                option_two = temp
            return option_two

        
        return max(howMuch(0, len(nums) - 2), howMuch(1, len(nums) - 1))

        