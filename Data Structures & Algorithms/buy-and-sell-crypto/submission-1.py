class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxP = 0;
        while end < len(prices):
            if prices[start] >= prices[end]:
                start += 1
                end += 1
            else:
                maxP = max(maxP, (prices[end] - prices[start]))
                end += 1
        return maxP
        