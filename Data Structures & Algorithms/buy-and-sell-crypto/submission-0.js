class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;
        let b = prices[0];
        for(let price of prices) {
            if(price > b) maxProfit = Math.max(maxProfit, (price - b));
            else b = price;
        }
        return maxProfit;
    }
}
