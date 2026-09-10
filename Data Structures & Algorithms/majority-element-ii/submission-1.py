class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # count_nums = Counter(nums)
        # target = len(nums) / 3
        # res = []

        # for key, value in count_nums.items():
        #     if value > target:
        #         res.append(key)
        # return res
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # 1. Find the two candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # 2. Verify the candidates
        result = []
        threshold = len(nums) // 3

        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        if count1 > threshold:
            result.append(candidate1)

        if count2 > threshold:
            result.append(candidate2)

        return result