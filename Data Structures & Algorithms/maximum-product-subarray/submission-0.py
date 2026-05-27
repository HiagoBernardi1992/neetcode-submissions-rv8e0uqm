class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        maximum = max(nums)

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
            else:
                temp = n * currMax
                currMax = max(n * currMax, n * currMin, n)
                currMin = min(temp, n * currMin, n)
                maximum = max(maximum, currMax)
        return maximum


        