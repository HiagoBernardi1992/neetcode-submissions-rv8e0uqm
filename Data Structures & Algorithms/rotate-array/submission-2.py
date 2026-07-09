class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - k
        while r < len(nums):
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp
            r += 1
            l += 1