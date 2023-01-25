class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(n, cache):
            if n <= 2:
                return n
            
            if n in cache:
                return cache[n]

            cache[n] = climb(n-2, cache) + climb(n-1, cache)
            return cache[n]
        return climb(n, cache)
        