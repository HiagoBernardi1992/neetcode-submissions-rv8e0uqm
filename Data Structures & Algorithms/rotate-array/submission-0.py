class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - k
        while r < len(nums):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r += 1
        