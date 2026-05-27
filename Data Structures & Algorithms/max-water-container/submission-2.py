class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            d = r - l
            h = min(heights[l], heights[r])
            maxWater = max(maxWater, (d * h))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater