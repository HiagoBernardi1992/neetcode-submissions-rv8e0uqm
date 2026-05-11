class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        sellDay = 1
        maxP = 0;
        while sellDay < len(prices):
            if prices[sellDay] > prices[buyDay]:
                profit = prices[sellDay] - prices[buyDay]
                maxP = max(maxP, profit)                
            else:
                buyDay = sellDay
            sellDay += 1

        return maxP
        