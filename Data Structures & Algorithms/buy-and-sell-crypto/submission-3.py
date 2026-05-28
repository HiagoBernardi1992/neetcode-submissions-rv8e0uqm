class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = prices[0]

        for p in prices:
            if b >= p:
                b = p
            else:
                profit = max(profit, p - b)

        return profit