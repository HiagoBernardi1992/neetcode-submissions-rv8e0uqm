class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        start = 0
        while start in numbers:
            start += 1

        return start