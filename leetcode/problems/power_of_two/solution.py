class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n == 1 or (self.isPowerOfTwo(n/2) and n%2 ==0)

        