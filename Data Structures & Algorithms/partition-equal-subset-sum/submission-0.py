class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        possible_sums = set()
        possible_sums.add(0)
        possible_sums.add(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            for p in possible_sums.copy():
                val = nums[i] + p
                if val == target:
                    return True
                if val not in possible_sums:
                    possible_sums.add(val)
        return False
