class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit1, max_profit2  = 0, 0
        min_price1, min_price2 = float('inf'), float('inf')
        for i in prices:
            min_price1 = min(i, min_price1)
            max_profit1 = max(max_profit1, i - min_price1)
            min_price2 = min(min_price2, i - max_profit1)
            max_profit2 = max(max_profit2, i - min_price2)
        return max_profit2
        