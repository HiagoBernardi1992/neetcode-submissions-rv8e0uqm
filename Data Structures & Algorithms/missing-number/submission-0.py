class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        for n in nums:
            if n != start:
                return start
            start += 1