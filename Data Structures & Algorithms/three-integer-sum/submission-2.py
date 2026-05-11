class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue

            start = index  + 1
            end = len(nums) - 1
            while start < end:
                sum = num + nums[start] + nums[end]
                if sum > 0:
                    end -= 1
                elif sum < 0: 
                    start += 1
                else:
                    res.append([num, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        
        return res
