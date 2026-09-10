class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        target = len(nums) / 3
        res = []

        for key, value in count_nums.items():
            if value > target:
                res.append(key)
        return res