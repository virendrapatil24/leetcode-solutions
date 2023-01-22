class Solution:
    def tribonacci(self, n: int, cache={}) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        elif n in cache:
            return cache[n] 

        cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return cache[n]