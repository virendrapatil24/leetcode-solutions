class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = prices[0], 0
        for price in prices:
            if price < i:
                i = price
            if j < price - i:
                j = price - i
        return j
            

        