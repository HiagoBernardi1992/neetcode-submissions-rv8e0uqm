class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expectedList = {}
        for i, val in enumerate(nums):
            expected = target - val
            if expected in expectedList:
                return [expectedList[expected], i]
            else:
                expectedList[val] = i

        