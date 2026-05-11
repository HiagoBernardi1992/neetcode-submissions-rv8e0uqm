class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxWater = 0
        while start < end:
            distance = end  - start
            minHeigth = min(heights[start], heights[end])
            water = distance * minHeigth
            maxWater = max(maxWater, water)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return maxWater