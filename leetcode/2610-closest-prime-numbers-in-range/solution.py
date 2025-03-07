class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.get_primes(left, right)
        if len(primes) < 2:
            return [-1, -1]
        diff = right
        res = []
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]
        return res
    
    def get_primes(self, left, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if not is_prime[i]:
                continue
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
        primes = []
        for i in range(left, n + 1):
            if is_prime[i]:
                primes.append(i)
        return primes


        
