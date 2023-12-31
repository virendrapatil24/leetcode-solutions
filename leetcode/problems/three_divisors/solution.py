class Solution:
    def isThree(self, n: int) -> bool:
        p = int(n ** 0.5)
        if p * p != n or p <= 1:
            return False
        if p <= 3:
            return True
        if p % 2 == 0 or p % 3 == 0:
            return False
        i = 5
        while i ** 2 < p:
            if p % i == 0 or p % i + 2 == 0:
                return False
            i += 6

        return True
        