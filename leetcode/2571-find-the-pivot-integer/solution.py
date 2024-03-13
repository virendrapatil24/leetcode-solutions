class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return 1
        n_sum = n * (n + 1) // 2
        for x in range(1, n):
            x_sum = x * (x + 1) // 2
            if 2 * x_sum == n_sum + x:
                return x
        return -1
        
