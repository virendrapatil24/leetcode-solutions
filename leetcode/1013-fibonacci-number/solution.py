class Solution:
    def fib(self, n: int, cache={}) -> int:
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self.fib(n-1) + self.fib(n-2) 
        return cache[n]
        
