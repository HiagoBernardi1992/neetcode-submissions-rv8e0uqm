class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = nums[0]
        rob2 = nums[1]

        for n in nums[2:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2