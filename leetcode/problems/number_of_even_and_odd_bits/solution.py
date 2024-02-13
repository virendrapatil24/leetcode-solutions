class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        while n:
            if n & 1: even += 1
            n = n >> 1
            if n == 0: break
            if n & 1: odd += 1
            n = n >> 1
        return [even, odd]
        
        