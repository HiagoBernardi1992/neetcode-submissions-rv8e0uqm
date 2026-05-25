class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        response = [1] * len(nums)
        prefix = 1
        for i, n in enumerate(nums):
            response[i] = prefix
            prefix *= n

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            response[i] *= suffix
            suffix *= nums[i]

        return response
