class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a
        