class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expected = {}
        for index, n in enumerate(nums):
            if (target - n) in expected:
                return [expected[(target - n)], index]
            else:
                expected[n] = index

        