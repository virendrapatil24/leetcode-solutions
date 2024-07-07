class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            res += exchange
            numBottles = exchange + numBottles % numExchange
        return res
        
