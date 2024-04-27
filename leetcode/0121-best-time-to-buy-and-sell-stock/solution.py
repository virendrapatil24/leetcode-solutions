class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_profit = prices[0], 0
        for price in prices:
            if price < min_val:
                min_val = price
            if max_profit < price - min_val:
                max_profit = price - min_val
        return max_profit
        
