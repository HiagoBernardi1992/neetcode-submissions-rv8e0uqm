class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        response = [1] * length
        prefix = 1
        for index, num in enumerate(nums):
            response[index] = prefix
            prefix *= num

        suffix = 1
        for index in range(length - 1, -1, -1):
            response[index] *= suffix
            suffix *= nums[index]

        return response

        