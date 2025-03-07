class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9 + 7)

        def countGood(x, n):
            if n == 0:
                return 1
            
            if n % 2 == 0:
                return countGood(x * x  % MOD, n // 2)
            else:
                return x * countGood(x, n - 1) % MOD
        
        return 5 ** (n % 2) * countGood(4 * 5, n // 2) % MOD
        
