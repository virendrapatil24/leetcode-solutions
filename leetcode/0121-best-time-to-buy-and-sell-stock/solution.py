class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_profit = inf, 0
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)
        return max_profit
        
