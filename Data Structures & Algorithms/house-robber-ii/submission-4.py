class Solution:
    def rob(self, nums: List[int]) -> int:

        def howMuch(nums):
            option_one = 0
            option_two = 0
            for n in nums:
                temp = max(option_one + n, option_two)
                option_one = option_two
                option_two = temp
            return option_two

        o1 = nums[:len(nums) - 1]
        o2 = nums[1:]
        return max(howMuch(o1), howMuch(o2))

        