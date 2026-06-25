class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            calc = numbers[l] + numbers[r]
            if calc == target:
                return [numbers[l], numbers[r]]
            elif calc > target:
                r -= 1
            else:
                l += 1


        